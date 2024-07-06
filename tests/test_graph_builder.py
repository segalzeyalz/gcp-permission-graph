import json

import pytest
from src.graph.graph import Graph
from src.graph.graph_node import NodeType
from src.graph.edge import EdgeType
from src.builder.graph_builder import GraphBuilder
from src.parser.graph_json_parser import GraphJsonParser

@pytest.fixture
def setup_json_file(tmp_path):
    data = [
        {"resource_id": "organization1", "type": "organization", "ancestors": [], "bindings": []},
        {"resource_id": "folder1", "type": "folder", "ancestors": ["folder1", "organization1"], "bindings": []},
        {"resource_id": "folder2", "type": "folder", "ancestors": ["folder2", "organization1"], "bindings": []},
        {"resource_id": "folder3", "type": "folder", "ancestors": ["folder3", "folder1", "organization1"],
         "bindings": []},
        {"resource_id": "resource1", "type": "resource", "ancestors": ["resource1", "folder1", "organization1"],
         "bindings": [{"role": "owner", "members": ["user:alex@test.authomize.com"]}]},
        {"resource_id": "resource2", "type": "resource", "ancestors": ["resource2", "folder2", "organization1"],
         "bindings": [{"role": "editor", "members": ["user:alex@test.authomize.com"]},
                      {"role": "viewer", "members": ["user:ron@test.authomize.com"]}]}
    ]

    file_path = tmp_path / "example.jsonl"
    with open(file_path, 'w') as f:
        for line in data:
            f.write(f"{json.dumps(line)}\n")

    return file_path


def test_graph_builder(setup_json_file):
    graph = Graph()
    parser = GraphJsonParser()
    builder = GraphBuilder(graph, parser)
    builder.build_graph(setup_json_file)

    # Check nodes
    expected_nodes = [
        ("organization1", NodeType.RESOURCE),
        ("folder1", NodeType.RESOURCE),
        ("folder2", NodeType.RESOURCE),
        ("folder3", NodeType.RESOURCE),
        ("resource1", NodeType.RESOURCE),
        ("resource2", NodeType.RESOURCE),
        ("user:alex@test.authomize.com", NodeType.IDENTITY),
        ("user:ron@test.authomize.com", NodeType.IDENTITY)
    ]

    for node_id, node_type in expected_nodes:
        assert node_id in graph.nodes, f"Node {node_id} should be in the graph"
        assert graph.nodes[node_id].type == node_type, f"Node {node_id} should be of type {node_type.name}"

    # Check edges
    expected_edges = [
        ("organization1", "folder1", EdgeType.PARENT),
        ("organization1", "folder2", EdgeType.PARENT),
        ("folder1", "folder3", EdgeType.PARENT),
        ("folder1", "resource1", EdgeType.PARENT),
        ("folder2", "resource2", EdgeType.PARENT),
        ("user:alex@test.authomize.com", "resource1", EdgeType.PERMISSION),
        ("user:alex@test.authomize.com", "resource2", EdgeType.PERMISSION),
        ("user:ron@test.authomize.com", "resource2", EdgeType.PERMISSION)
    ]

    edges_set = set((e.from_node.id, e.to_node.id, e.type) for e in graph.edges)
    for from_id, to_id, edge_type in expected_edges:
        assert (from_id, to_id,
                edge_type) in edges_set, f"Edge from {from_id} to {to_id} of type {edge_type.name} should be in the graph"
