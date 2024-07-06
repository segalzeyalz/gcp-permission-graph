# example_usage.py
from src.graph.graph import Graph
from src.graph.graph_node import GraphNode, NodeType
from src.graph.edge import Edge, EdgeType


def build_example_graph():
    graph = Graph()

    # Adding nodes
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

    # Adding edges
    edges = [
        Edge(graph.nodes["organization1"], graph.nodes["folder1"], EdgeType.PARENT),
        Edge(graph.nodes["organization1"], graph.nodes["folder2"], EdgeType.PARENT),
        Edge(graph.nodes["folder1"], graph.nodes["folder3"], EdgeType.PARENT),
        Edge(graph.nodes["folder1"], graph.nodes["resource1"], EdgeType.PARENT),
        Edge(graph.nodes["folder2"], graph.nodes["resource2"], EdgeType.PARENT),
        Edge(graph.nodes["user:alex@test.authomize.com"], graph.nodes["resource1"], EdgeType.PERMISSION, "owner"),
        Edge(graph.nodes["user:alex@test.authomize.com"], graph.nodes["resource2"], EdgeType.PERMISSION, "editor"),
        Edge(graph.nodes["user:ron@test.authomize.com"], graph.nodes["resource2"], EdgeType.PERMISSION, "viewer")
    ]

    for edge in edges:
        graph.add_edge(edge)

    return graph

def main():
    graph = build_example_graph()

    # Query the graph
    print("Resource Hierarchy for 'resource1':", graph.get_resource_hierarchy("resource1"))
    print("Permissions for 'user:alex@test.authomize.com':",
          graph.get_identity_permissions("user:alex@test.authomize.com"))
    print("Identities with permissions on 'resource2':", graph.get_resource_identities("resource2"))


if __name__ == "__main__":
    main()
