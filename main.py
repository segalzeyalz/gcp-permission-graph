import argparse
from src.graph.graph import Graph
from src.parser.graph_json_parser import GraphJsonParser
from src.builder.graph_builder import GraphBuilder

def main():
    parser = argparse.ArgumentParser(description="Build a permission graph from a JSON lines file")
    parser.add_argument('json_file', type=str, help="Path to the JSON lines file containing the permission model")
    parser.add_argument('--resource-hierarchy', type=str, help="Get the hierarchy of the given resource ID")
    parser.add_argument('--identity-permissions', type=str, help="Get the permissions of the given identity ID")
    parser.add_argument('--resource-identities', type=str, help="Get the identities with permissions on the given resource ID")

    args = parser.parse_args()

    # Initialize the components
    graph = Graph()
    parser = GraphJsonParser()
    builder = GraphBuilder(graph, parser)

    # Build the graph using the configuration
    builder.build_graph(args.json_file)

    if args.resource_hierarchy:
        hierarchy = graph.get_resource_hierarchy(args.resource_hierarchy)
        print(f"Hierarchy for resource '{args.resource_hierarchy}': {hierarchy}")

    if args.identity_permissions:
        permissions = graph.get_identity_permissions(args.identity_permissions)
        print(f"Permissions for identity '{args.identity_permissions}': {permissions}")

    if args.resource_identities:
        identities = graph.get_resource_identities(args.resource_identities)
        print(f"Identities with permissions on resource '{args.resource_identities}': {identities}")

if __name__ == "__main__":
    main()
