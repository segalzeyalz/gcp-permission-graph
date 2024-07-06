import pytest
from src.graph.graph_node import GraphNode, NodeType
def test_graph_node_creation():
    node = GraphNode(id="node1", type=NodeType.IDENTITY)
    assert node.id == "node1", "Node ID should be 'node1'"
    assert node.type == NodeType.IDENTITY, "Node type should be 'IDENTITY' as the constructor"

def test_graph_node_get_id():
    node = GraphNode(id="node2", type=NodeType.RESOURCE)
    assert node.get_id() == "node2", "get_id() should return 'node2' as id inserted"
def test_graph_node_get_type():
    node = GraphNode(id="node3", type=NodeType.RESOURCE)
    assert node.get_type() == "RESOURCE", "get_type() should return 'RESOURCE' - as this is the type"

def test_graph_node_equality():
    node1 = GraphNode(id="node1", type=NodeType.IDENTITY)
    node2 = GraphNode(id="node1", type=NodeType.IDENTITY)
    assert node1 == node2, "Nodes with the same ID and type should be equal"

def test_graph_node_inequality():
    node1 = GraphNode(id="node1", type=NodeType.IDENTITY)
    node2 = GraphNode(id="node2", type=NodeType.IDENTITY)
    assert node1 != node2, "Nodes with different IDs should not be equal"

    node3 = GraphNode(id="node1", type=NodeType.RESOURCE)
    assert node1 != node3, "Nodes with the same ID but different types should not be equal"
