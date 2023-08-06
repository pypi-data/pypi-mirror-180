import heapq
import random
from typing import Any, Hashable, Sequence

from kumo.errors import DuplicatedError, EmptyStorageError
from kumo.storage.funcs import get_index_value
from kumo.types import (IndexSpec, Node, NodeData, NodeGetStrategy, NodeMeta,
                        PutBackStatus)


class MemoryCollection:
    def __init__(self, node: Node, unique_constraints: Sequence[IndexSpec], get_strategy: NodeGetStrategy):
        self.node = node
        self.data: list[tuple[NodeData, NodeMeta]] = []
        self.unique_indexes: dict[IndexSpec, dict[Hashable, int]] = {s: {} for s in unique_constraints}
        self.get_strategy = get_strategy
        self.new_set: set[int] = set()
        self.heap: list[tuple[float,float,int]] = []

    def put(self, data: NodeData):
        indexes_data = [(v, get_index_value(data, s)) for s, v in self.unique_indexes.items()]

        for index, index_value in indexes_data:
            if index_value in index:
                raise DuplicatedError()

        next_loc = len(self.data)
        
        for index, index_value in indexes_data:
            index[index_value] = next_loc
        
        self.new_set.add(next_loc)
        
        self.data.append((data, NodeMeta()))
    
    def get(self) -> NodeData:
        if len(self.new_set) > 0 and len(self.heap) > 0:
            if random.random() < self.get_strategy.exploration_prob:
                return self.explore()
            
            return self.exploit()
            
        if len(self.heap) > 0:
            return self.exploit()
        
        if len(self.new_set) > 0:
            return self.explore()
        
        raise EmptyStorageError(self.node)

    def explore(self) -> NodeData:
        loc = random.sample(self.new_set, 1)[0]
        self.new_set.remove(loc)

        return self.data[loc][0]
    
    def exploit(self) -> NodeData:
        return self.data[heapq.heappop(self.heap)[2]][0]

    def put_back(self, data: NodeData, status: PutBackStatus):
        loc = self.get_loc(data)

        data, meta = self.data[loc]

        meta.n_errors += status.n_errors
        meta.n_duplicated += status.n_duplicated
        meta.n_generated += status.n_generated
        meta.n_attempted += 1

        if self.get_strategy.max_errors is not None and meta.n_errors > self.get_strategy.max_errors:
            return

        if self.get_strategy.max_duplicated is not None and meta.n_duplicated > self.get_strategy.max_duplicated:
            return

        if meta.n_attempted >= self.get_strategy.n_exploration_attempts:
            heapq.heappush(self.heap, (-meta.n_generated / meta.n_attempted, random.random(), loc))
            return
        
        self.new_set.add(loc)
        
    def get_loc(self, data: NodeData) -> int:
        index_spec, index = next(iter(self.unique_indexes.items()))

        index_value = get_index_value(data, index_spec)

        loc = index[index_value]

        if self.data[loc][0] != data:
            raise ValueError(f"Data changed, {data} != {self.data[loc][0]}")

        return loc

class MemoryStorage:
    def __init__(self, get_strategy: NodeGetStrategy | None = None):
        self.nodes: list[Node] = []
        self.store: dict[Node, MemoryCollection] = {}
        self.get_strategy = NodeGetStrategy() if get_strategy is None else get_strategy
    
    def add_node(self, node: Node, unique_constraints: Sequence[str | tuple[str, ...]]):
        self.nodes.append(node)
        self.store[node] = MemoryCollection(node, unique_constraints, self.get_strategy)

    def get(self, node: Node) -> Any:
        return self.store[node].get()

    def put(self, data: Any):
        self.store[type(data)].put(data)

    def put_back(self, data: Any, status: PutBackStatus):
        self.store[type(data)].put_back(data, status)