from __future__ import annotations
from dataclasses import dataclass, asdict
import os
from typing import List, Optional, Sequence, Union
import typing
import typer
import jsonpickle
import treeswift as ts
import numpy as np
import pandas as pd
import json
from structlog import get_logger

from hm01.basics import Graph, IntangibleSubgraph
from .leiden_wrapper import LeidenClusterer


class ClusteringMetadata:
    """Metadata about a clustering as recorded in a tree."""

    def __init__(self, tree: ts.Tree):
        self.tree = tree
        self.lookup = {}
        for n in tree.traverse_postorder():
            self.lookup[n.label] = n

    def find_info(self, graph: Union[Graph, IntangibleSubgraph]) -> Optional[ts.Node]:
        """Find the info for the graph"""
        return self.lookup.get(graph.index)


def summary_list(list: Sequence[Union[int, float]]) -> str:
    """Summarize a list of numbers"""
    return f"{min(list)}-{np.median(list)}-{max(list)}"


def read_clusters_from_leiden(filepath: str) -> List[IntangibleSubgraph]:
    clusterer = LeidenClusterer(1)
    return clusterer.from_existing_clustering(filepath)


@dataclass
class ClusteringSkeleton:
    label: str
    nodes: List[int]
    connectivity: int
    descendants: List[str]

    @staticmethod
    def from_graphs(
        global_graph: Graph,
        graphs: List[IntangibleSubgraph],
        metadata: ClusteringMetadata,
    ) -> List[ClusteringSkeleton]:
        ans = []
        for g in graphs:
            info = metadata.find_info(g)
            if info:
                # hack because I accidentally left out the ``cut_size'' attribute when pruning
                if not hasattr(info, "cut_size"):
                    info.cut_size = g.count_mcd(global_graph)
            descendants = []
            for n in info.traverse_leaves():
                if n.label != g.index:
                    descendants.append(n.label)
            ans.append(
                ClusteringSkeleton(
                    g.index, list(g.nodes), info.cut_size if info else 1, descendants
                )
            )
        ans.sort(key=lambda x: (len(x.descendants), len(x.nodes)), reverse=True)
        return ans

    @staticmethod
    def write_ndjson(graphs: List[ClusteringSkeleton], filepath: str):
        use_descendants = False
        if any(g.descendants for g in graphs):
            use_descendants = True
        with open(filepath, "w+") as f:
            for g in graphs:
                d = asdict(g)
                if not use_descendants:
                    del d["descendants"]
                f.write(json.dumps(d) + "\n")


@dataclass
class ClusteringStats:
    num_clusters: int
    total_nodes: int
    total_edges: int
    top_singleton_nodes: int
    min_cut_sizes: List[int]
    cluster_sizes: List[int]

    def to_stats(self, global_graph: Graph) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "num_clusters": [self.num_clusters],
                "node_coverage": [self.total_nodes / global_graph.n()],
                "total_nodes": [self.total_nodes],
                "edge_coverage": [self.total_edges / global_graph.m()],
                "total_edges": [self.total_edges],
                "top_singleton_nodes": [self.top_singleton_nodes],
                "min_cut_sizes": [summary_list(self.min_cut_sizes)],
                "cluster_sizes": [summary_list(self.cluster_sizes)],
            }
        )

    @staticmethod
    def from_list_of_graphs(
        global_graph: Graph,
        graphs: List[IntangibleSubgraph],
        metadata: ClusteringMetadata,
    ):
        num_clusters = 0
        total_nodes = 0
        total_edges = 0
        min_cut_sizes: List[int] = []
        cluster_sizes: List[int] = []
        included_nodes = set()
        for g in graphs:
            if g.n() == 0:
                continue
            num_clusters += 1
            total_nodes += g.n()
            total_edges += g.count_edges(global_graph)
            info = metadata.find_info(g)
            if info:
                # hack because I accidentally left out the ``cut_size'' attribute when pruning
                if not hasattr(info, "cut_size"):
                    info.cut_size = g.count_mcd(global_graph)
            min_cut_sizes.append(info.cut_size if info else 1)
            cluster_sizes.append(g.n())
            included_nodes.update(g.nodes)
        ninty_percentile_degree = np.percentile(
            [global_graph.data.degree(n) for n in global_graph.nodes()], 90
        )
        top_singleton_nodes = (
            sum(
                1
                for n in global_graph.nodes()
                if global_graph.data.degree(n) >= ninty_percentile_degree
                and n not in included_nodes
            )
            / global_graph.n()
        )
        return ClusteringStats(
            num_clusters,
            total_nodes,
            total_edges,
            top_singleton_nodes,
            min_cut_sizes,
            cluster_sizes,
        )


def main(
    input: str = typer.Option(..., "--input", "-i"),
    graph_path: str = typer.Option(..., "--graph", "-g"),
    output: str = typer.Option(..., "--output_prefix", "-o"),
    ancient_clustering_path: Optional[str] = typer.Option(None, "--ancient_clustering"),
):
    """Compute two sets of statistics for a hiearchical clustering"""
    log = get_logger()
    assert os.path.exists(input)
    treepath = input + ".tree.json"
    assert os.path.exists(treepath)
    assert os.path.exists(graph_path)
    graph = Graph.from_edgelist(graph_path)
    log.info("loaded graph", graph_n=graph.n(), graph_m=graph.m())
    with open(treepath, "r") as f:
        tree: ts.Tree = typing.cast(ts.Tree, jsonpickle.decode(f.read()))
    for n in tree.traverse_postorder():
        n.nodes = []
    metadata = ClusteringMetadata(tree)
    node2cid = {}
    with open(input, "r") as f:
        for l in f:
            node, cid = l.strip().split()
            node2cid[int(node)] = cid
            metadata.lookup[cid].nodes.append(int(node))
    log.info("loaded clustering")
    for c in tree.root.children:
        c.nodes = list(set.union(*[set(n.nodes) for n in c.traverse_postorder()]))
    original_clusters = [
        IntangibleSubgraph(n.nodes, n.label) for n in tree.root.children
    ]
    extant_clusters = [
        IntangibleSubgraph(n.nodes, n.label) for n in tree.traverse_leaves() if n.extant
    ]
    original_skeletons = ClusteringSkeleton.from_graphs(
        graph, original_clusters, metadata
    )
    extant_skeletons = ClusteringSkeleton.from_graphs(graph, extant_clusters, metadata)
    ClusteringSkeleton.write_ndjson(original_skeletons, output + ".original.json")
    ClusteringSkeleton.write_ndjson(extant_skeletons, output + ".extant.json")


def entry_point():
    typer.run(main)


if __name__ == "__main__":
    entry_point()
