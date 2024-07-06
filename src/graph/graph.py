from collections import defaultdict

from src.graph.edge import Edge, EdgeType
from src.graph.graph_node import GraphNode


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.parent_map = {}
        self.permission_map = defaultdict(list) #nice trick ^_^ to avoid the if and assignment of []

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

        # Maintain parent_map
        if edge.type == EdgeType.PARENT:
            self.parent_map[edge.to_node.id] = edge.from_node  # Storing parent node object

        # Maintain permission_map
        if edge.type == EdgeType.PERMISSION:
            self.permission_map[edge.to_node.id].append((edge.from_node.id, edge.type.name))

    def get_resource_hierarchy(self, resource_id: str):
        """
        Get the hierarchy of a given resource.
        :param resource_id: The ID of the resource.
        :return: A list of ancestor resource IDs in hierarchical order.
        """
        hierarchy = []
        current_node = self.nodes.get(resource_id)
        while current_node:
            parent_node = self.parent_map.get(current_node.id)
            if parent_node:
                hierarchy.append(parent_node.id)
                current_node = parent_node
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
        for resource_id, roles in self.permission_map.items():
            for from_node_id, role in roles:
                if from_node_id == identity_id:
                    resource_type = self.nodes[resource_id].type.name
                    permissions.append((resource_id, resource_type, role))
        return permissions

    def get_resource_identities(self, resource_id: str):
        """
        Get all identities and roles for a given resource.
        :param resource_id: The ID of the resource.
        :return: A list of tuples (identity_id, role).
        """
        return self.permission_map.get(resource_id, [])