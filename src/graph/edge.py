from dataclasses import dataclass
from enum import Enum, auto

from src.graph.graph_node import GraphNode


class EdgeType(Enum):
    """
    Enum class for the type of edge in the graph
    """
    PARENT = auto()
    PERMISSION = auto()

@dataclass
class Edge:
    from_node: GraphNode
    to_node: GraphNode
    type: EdgeType
    role: str = None