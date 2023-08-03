from node_type import NodeType


class Node:
    """Class represents a Node from a Reaper Project File tree."""

    def __init__(self, ntype: NodeType) -> None:
        self.type = ntype
        self.inner = []         # list of Nodes
        self.prev = None
        self.parameters = []    # list of Parameters
        self.depth = 0          # 0 = head, maximal value = distance of leaf

    def __str__(self) -> str:       
        return f"{self.prev} -> {self.type}.[{len(self.inner)} /{self.depth}]"

    def print_tree(self) -> None:
        """Prints node tree, starting from itself as the main node"""
        print(self)
        for p in self.parameters:
            print(p)
        for n in self.inner:
            print(n)
            for p in n.parameters:
                print(p)
            for n_2 in n.inner:
                print(n_2)
                print(n_2.parameters)
