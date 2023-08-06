from dataclasses import dataclass
from typing import Any, Callable, Coroutine, Dict, List, Protocol, Tuple, Union


@dataclass
class NodeMeta:
    n_errors: int = 0
    n_duplicated: int = 0
    n_generated: int = 0
    n_attempted: int = 0

@dataclass
class NodeGetStrategy:
    max_errors: "int | None" = 3
    max_duplicated: "int | None" = None
    exploration_prob: float = 0.5
    n_exploration_attempts: int = 3

Node = type

NodeData = Any

Edge = Callable[[NodeData], Coroutine[Any, Any, List[NodeData]]]

Counts = Dict[Node, int]

IndexSpec = Union[str, Tuple[str, ...]]

@dataclass
class PutBackStatus:
    n_errors: int = 0
    n_duplicated: int = 0
    n_generated: int = 0

class Storage(Protocol):
    def get(self, node: Node) -> NodeData:
        pass

    def put(self, data: NodeData):
        pass
    
    def put_back(self, data: NodeData, status: PutBackStatus):
        pass
