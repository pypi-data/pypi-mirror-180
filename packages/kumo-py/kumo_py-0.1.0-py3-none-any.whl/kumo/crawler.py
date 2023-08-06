import asyncio
import random
from asyncio import Queue
from typing import TypeVar

from kumo.edge import CrawlerEdge
from kumo.errors import DuplicatedError, EdgeError
from kumo.types import Counts, Edge, Node, PutBackStatus, Storage

E = TypeVar("E", bound=Edge)
N = TypeVar("N", bound=Node)


class Crawler:
    def __init__(self, storage: Storage):
        self.edges: list[CrawlerEdge] = []
        self.storage = storage

        self._requested: Queue[Counts] = Queue()
        self._available: Counts = {}

    def edge(self):
        def decorator(func: E) -> E:
            self.edges.append(CrawlerEdge.from_func(func))
            return func
        return decorator

    async def request(self, counts:Counts):
        await self._requested.put(counts)

    async def _process_edge(self, edge: CrawlerEdge):
        input_data = self.storage.get(edge.input_node)

        try:
            output_data = await edge(input_data)
        except EdgeError as e:
            print(e)
            self.storage.put_back(input_data, PutBackStatus(1, 0, 0))
            return

        n_duplicated = 0
        n_generated = 0

        for data in output_data:
            try:
                self.storage.put(data)
                n_generated += 1
            except DuplicatedError:
                n_duplicated += 1

        self.storage.put_back(input_data, PutBackStatus(0, n_duplicated, n_generated))                

    def strategy(self) -> CrawlerEdge:
        return random.choice(self.edges)

    async def loop(self):
        while True:
            edge = self.strategy()
            await self._process_edge(edge)
            
    def run(self):
        asyncio.run(self.loop())
