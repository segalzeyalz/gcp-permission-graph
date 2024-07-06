import pytest
from src.graph.edge import Edge, EdgeType
from src.graph.graph_node import GraphNode, NodeType

def test_edge_creation():
    from_node = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge_type = EdgeType.PERMISSION

    edge = Edge(from_node=from_node, to_node=to_node, type=edge_type)

    assert edge.from_node == from_node, "The from_node should be correctly set in the edge"
    assert edge.to_node == to_node, "The to_node should be correctly set in the edge"
    assert edge.type == edge_type, "The type should be correctly set in the edge"

def test_edge_types():
    from_node = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node = GraphNode(id="node2", type=NodeType.RESOURCE)

    permission_edge = Edge(from_node=from_node, to_node=to_node, type=EdgeType.PERMISSION)
    parent_edge = Edge(from_node=from_node, to_node=to_node, type=EdgeType.PARENT)

    assert permission_edge.type == EdgeType.PERMISSION, "The edge type should be PERMISSION"
    assert parent_edge.type == EdgeType.PARENT, "The edge type should be PARENT"

def test_edge_comparison():
    from_node1 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node1 = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge1 = Edge(from_node=from_node1, to_node=to_node1, type=EdgeType.PERMISSION)

    from_node2 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node2 = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge2 = Edge(from_node=from_node2, to_node=to_node2, type=EdgeType.PERMISSION)

    assert edge1 == edge2, "Edges with the same from_node, to_node, and type should be equal"

def test_edge_not_equal():
    from_node1 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node1 = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge1 = Edge(from_node=from_node1, to_node=to_node1, type=EdgeType.PERMISSION)

    from_node2 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node2 = GraphNode(id="node3", type=NodeType.RESOURCE)
    edge2 = Edge(from_node=from_node2, to_node=to_node2, type=EdgeType.PERMISSION)

    assert edge1 != edge2, "Edges with different nodes or types should not be equal"

def test_edge_with_different_types():
    from_node1 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node1 = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge1 = Edge(from_node=from_node1, to_node=to_node1, type=EdgeType.PERMISSION)

    from_node2 = GraphNode(id="node1", type=NodeType.IDENTITY)
    to_node2 = GraphNode(id="node2", type=NodeType.RESOURCE)
    edge2 = Edge(from_node=from_node2, to_node=to_node2, type=EdgeType.PARENT)

    assert edge1 != edge2, "Edges with different types should not be equal"
