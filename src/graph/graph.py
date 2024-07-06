from src.graph.edge import Edge, EdgeType
from src.graph.graph_node import GraphNode


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: GraphNode):
        """
        Add a node to the graph
        :param node:
        """
        if node.id not in self.nodes:
            self.nodes[node.id] = node

    def add_edge(self, edge: Edge):
        """
        Add an edge to the graph
        :param edge:
        """
        self.edges.append(edge)

    def get_resource_hierarchy(self, resource_id: str):
        """
        Get the hierarchy of a given resource.
        :param resource_id: The ID of the resource.
        :return: A list of ancestor resource IDs in hierarchical order.
        """
        hierarchy = []
        current_node = self.nodes.get(resource_id)
        while current_node:
            parent_edge = next(
                (edge for edge in self.edges if edge.to_node == current_node and edge.type == EdgeType.PARENT), None)
            if parent_edge:
                hierarchy.append(parent_edge.from_node.id)
                current_node = parent_edge.from_node
            else:
                current_node = None
        return hierarchy

    def get_identity_permissions(self, identity_id: str):
        """
        Get all resources and roles for a given identity.
        :param identity_id: The ID of the identity.
        :return: A list of tuples (resource_id, resource_type, role).
        """
        permissions = []
        for edge in self.edges:
            if edge.from_node.id == identity_id and edge.type == EdgeType.PERMISSION:
                permissions.append((edge.to_node.id, edge.to_node.type.name, edge.type.name))
        return permissions

    def get_resource_identities(self, resource_id: str):
        """
        Get all identities and roles for a given resource.
        :param resource_id: The ID of the resource.
        :return: A list of tuples (identity_id, role).
        """
        identities = []
        for edge in self.edges:
            if edge.to_node.id == resource_id and edge.type == EdgeType.PERMISSION:
                identities.append((edge.from_node.id, edge.type.name))
        return identities