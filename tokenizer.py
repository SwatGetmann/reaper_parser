from typing import List

class WrongTreeIndexError(ValueError):
    def __init__(self):
        super().__init__("You can't use indecies other than 1 or 0")

class Node:
    """Class represents a Node from a Reaper Project File tree."""
    def __init__(self, name: str) -> None:
        self.indexes = []
        self.nodes = []
        self.inner = []
        self.first_line = None
        self.prev = None
        self.depth = 0
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.prev} -> {self.name}.[D:{self.depth} N:{len(self.nodes)} I:{len(self.inner)}]"

    def print_tree(self) -> None:
        """Prints node tree, starting from itself as the main node"""
        print(self)
        for n in self.nodes:
            n.print_tree()
            
    def add_node(self, node: 'Node') -> None:
        node.prev = self
        node.depth = self.depth + 1
        self.nodes.append(node)
        self.indexes.append(1)
        
    def add_inner(self, line: str) -> None:
        self.inner.append(line)
        self.indexes.append(0)
        
    def fetch_nodes(self, name: str, collection: list = []) -> List['Node']:
        if self.name == name:
            collection.append(self)
        if self.nodes:
            for i in self.nodes:
                i.fetch_nodes(name, collection)
        return collection
    
    def save_str_tree(self) -> str:
        lines = []
        if self.first_line:
            lines.append(f"{' ' * self.depth * 2}<{self.first_line}")
        else:
            lines.append(f"{' ' * self.depth * 2}<{self.name}")
        
        inner_idx = 0
        nodex_idx = 0
        for index in self.indexes:
            if index == 0:
                lines += [f"{' ' * (self.depth+1) * 2}{self.inner[inner_idx]}"]
                inner_idx += 1
            elif index == 1:
                lines += self.nodes[nodex_idx].save_str_tree()
                nodex_idx += 1
            else:
                raise WrongTreeIndexError()
        lines.append(f"{' ' * self.depth * 2}>")
        return lines


def tokenize_node(stream) -> List[Node]:
    line_type = None
    node_curr = None
    
    lens = [len(l) for l in stream]
    max_line_len = max(lens)
    
    heads = []
    
    def context_msg():
        if node_curr:
            depth = node_curr.depth + 1
        else:
            depth = 0
        return f"{{{depth:2}}} : {str(line_type).ljust(10)} : {str(node_curr)}"

    for lidx, line in enumerate(stream):
        if line.lstrip()[0] == '<':
            line_type = 'TAG_OPEN'
            strip_line = line.lstrip()[1:]
            splits = strip_line.split(" ")
            node_name = splits[0].rstrip()
            node = Node(node_name)
            if len(splits) > 1:
                node.first_line = strip_line.rstrip()
            if node_curr:
                node_curr.add_node(node)
            node_curr = node
            if node_curr.depth == 0:
                heads.append(node_curr)
        elif line.lstrip()[0] == '>':
            line_type = 'TAG_CLOSE'
            node_curr = node_curr.prev
        else:
            line_type = 'TAG_INNER'
            node_curr.add_inner(line.strip())
        print(f"[{lidx:4}]: {line.rstrip().ljust(max_line_len)} | {context_msg()}")
    
    return heads
