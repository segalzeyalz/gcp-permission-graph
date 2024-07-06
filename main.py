from src.builder.graph_builder import GraphBuilder
from src.config.config import Config
from src.graph.graph import Graph
from src.parser.graph_json_parser import GraphJsonParser


def main():
    # Initialize configuration
    config = Config(json_file_path="data/example.json1")

    # Initialize the components
    graph = Graph()
    parser = GraphJsonParser()
    builder = GraphBuilder(graph, parser)

    # Build the graph using the configuration
    builder.build_graph(config.json_file_path)



if __name__ == "__main__":
    main()
