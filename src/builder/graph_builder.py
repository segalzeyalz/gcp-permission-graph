from src.graph.edge import Edge, EdgeType
from src.graph.graph import Graph
from src.graph.graph_node import GraphNode, NodeType
from src.parser.graph_json_parser import GraphJsonParser


class GraphBuilder:
    def __init__(self, graph: Graph, parser: GraphJsonParser):
        self.graph = graph
        self.parser = parser

    def build_graph(self, file_path: str):
        data = self.parser.parse(file_path)
        for resource in data:
            resource_node = GraphNode(resource['resource_id'], NodeType.RESOURCE)
            self.graph += resource_node  # Using the += operator to add nodes

            # Add ancestor edges
            ancestors = resource.get('ancestors', [])
            for i in range(1, len(ancestors)):
                parent_node = GraphNode(ancestors[i], NodeType.RESOURCE)
                self.graph += parent_node  # Using the += operator to add nodes
                self.graph.add_edge(Edge(parent_node, resource_node, EdgeType.PARENT))

            # Add permission bindings
            bindings = resource.get('bindings', [])
            for binding in bindings:
                role = binding['role']
                for member in binding['members']:
                    identity_node = GraphNode(member, NodeType.IDENTITY)
                    self.graph.add_node(identity_node)

                    edge = Edge(identity_node, resource_node, EdgeType.PERMISSION)
                    self.graph.add_edge(edge)
