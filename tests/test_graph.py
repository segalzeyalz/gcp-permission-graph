import pytest
from src.graph.graph import Graph
from src.graph.graph_node import GraphNode, NodeType
from src.graph.edge import Edge, EdgeType

@pytest.fixture
def setup_graph():
    graph = Graph()

    # Add nodes
    nodes = [
        GraphNode("organization1", NodeType.RESOURCE),
        GraphNode("folder1", NodeType.RESOURCE),
        GraphNode("folder2", NodeType.RESOURCE),
        GraphNode("folder3", NodeType.RESOURCE),
        GraphNode("resource1", NodeType.RESOURCE),
        GraphNode("resource2", NodeType.RESOURCE),
        GraphNode("user:alex@test.authomize.com", NodeType.IDENTITY),
        GraphNode("user:ron@test.authomize.com", NodeType.IDENTITY)
    ]
    for node in nodes:
        graph.add_node(node)

    # Add edges (parent-child relationships)
    parent_edges = [
        Edge(graph.nodes["organization1"], graph.nodes["folder1"], EdgeType.PARENT),
        Edge(graph.nodes["organization1"], graph.nodes["folder2"], EdgeType.PARENT),
        Edge(graph.nodes["folder1"], graph.nodes["folder3"], EdgeType.PARENT),
        Edge(graph.nodes["folder1"], graph.nodes["resource1"], EdgeType.PARENT),
        Edge(graph.nodes["folder2"], graph.nodes["resource2"], EdgeType.PARENT)
    ]
    for edge in parent_edges:
        graph.add_edge(edge)

    # Add edges (permissions)
    permission_edges = [
        Edge(graph.nodes["user:alex@test.authomize.com"], graph.nodes["resource1"], EdgeType.PERMISSION),
        Edge(graph.nodes["user:alex@test.authomize.com"], graph.nodes["resource2"], EdgeType.PERMISSION),
        Edge(graph.nodes["user:ron@test.authomize.com"], graph.nodes["resource2"], EdgeType.PERMISSION)
    ]
    for edge in permission_edges:
        graph.add_edge(edge)

    return graph

def test_get_resource_hierarchy(setup_graph):
    graph = setup_graph

    hierarchy = graph.get_resource_hierarchy("resource1")
    assert hierarchy == ["folder1", "organization1"], "Hierarchy of resource1 should be ['folder1', 'organization1']"

    hierarchy = graph.get_resource_hierarchy("folder3")
    assert hierarchy == ["folder1", "organization1"], "Hierarchy of folder3 should be ['folder1', 'organization1']"

def test_get_identity_permissions(setup_graph):
    graph = setup_graph

    permissions = graph.get_identity_permissions("user:alex@test.authomize.com")
    assert permissions == [("resource1", "RESOURCE", "PERMISSION"), ("resource2", "RESOURCE", "PERMISSION")], "Permissions for user:alex@test.authomize.com should be [('resource1', 'RESOURCE', 'PERMISSION'), ('resource2', 'RESOURCE', 'PERMISSION')]"

    permissions = graph.get_identity_permissions("user:ron@test.authomize.com")
    assert permissions == [("resource2", "RESOURCE", "PERMISSION")], "Permissions for user:ron@test.authomize.com should be [('resource2', 'RESOURCE', 'PERMISSION')]"

def test_get_resource_identities(setup_graph):
    graph = setup_graph

    identities = graph.get_resource_identities("resource1")
    assert identities == [("user:alex@test.authomize.com", "PERMISSION")], "Identities for resource1 should be [('user:alex@test.authomize.com', 'PERMISSION')]"

    identities = graph.get_resource_identities("resource2")
    assert identities == [("user:alex@test.authomize.com", "PERMISSION"), ("user:ron@test.authomize.com", "PERMISSION")], "Identities for resource2 should be [('user:alex@test.authomize.com', 'PERMISSION'), ('user:ron@test.authomize.com', 'PERMISSION')]"
