from typing import List
from node_type import NodeType


class Node:
    """Class represents a Node from a Reaper Project File tree."""

    def __init__(self, ntype: NodeType) -> None:
        self.type = ntype
        self.inner = []         # list of Nodes
        self.prev = None
        self.parameters = []    # list of Parameters
        self.parameters_first_line = []
        self.depth = 0          # 0 = head, maximal value = distance of leaf

    def __str__(self) -> str:       
        return f"{self.prev} -> {self.type}.[{len(self.inner)} /{self.depth}]"

    def print_tree(self) -> None:
        """Prints node tree, starting from itself as the main node"""
        print(self)
        print(self.parameters_first_line)
        for p in self.parameters:
            print(p)
        for n in self.inner:
            n.print_tree()
    
    def fetch(self, node_type: NodeType, collection: list) -> List['Node']:
        """Searches and provides a list of Nodes for a given NodeType.

        Returns:
            List[Node]: List of Nodes with a desired Node Type. \
                Can be empty.
        """
        if self.type == node_type:
            collection.append(self)
        if self.inner:
            for i in self.inner:
                i.fetch(node_type, collection)
        return collection
