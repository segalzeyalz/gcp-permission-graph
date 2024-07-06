from dataclasses import dataclass
from enum import Enum, auto


class NodeType(Enum):
    """
    Enum class for the type of node in the graph
    """
    IDENTITY = auto()
    RESOURCE = auto()

@dataclass
class GraphNode:
    id: str
    type: NodeType

    def get_id(self) -> str:
        return self.id

    def get_type(self) -> str:
        return self.type.name