from dataclasses import dataclass

from kumo.types import Edge, Node


@dataclass
class CrawlerEdge:
    input_node: Node
    output_node: Node
    func: Edge

    @classmethod
    def from_func(cls, func: Edge) -> "CrawlerEdge":
        annotations = func.__annotations__

        output_node = annotations.pop("return")

        if len(annotations) != 1:
            raise ValueError("Edge functions must have exactly one input")
        
        input_node = list(annotations.values())[0]

        return cls(input_node, output_node, func)

    async def __call__(self, input: Node) -> "list[Node]":
        return await self.func(input)
