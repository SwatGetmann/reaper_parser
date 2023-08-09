class Node:
    """Class represents a Node from a Reaper Project File tree."""
    def __init__(self, name: str) -> None:
        self.nodes = []
        self.inner = []
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
    
    def save_str_tree(self) -> str:
        lines = [f"{' ' * self.depth * 2}<{self.name}"]
        for i in self.inner:
            lines += [f"{' ' * (self.depth+1) * 2}{i}"]
        for n in self.nodes:
            lines += n.save_str_tree()
        lines.append(f"{' ' * self.depth * 2}>")
        return lines

def tokenize_node(stream):
    line_type = None
    node_curr = None
    
    lens = [len(l) for l in stream]
    max_line_len = max(lens)
    
    def context_msg():
        if node_curr:
            depth = node_curr.depth + 1
        else:
            depth = 0
        return f"{{{depth:2}}} : {str(line_type).ljust(10)} : {str(node_curr)}"

    for lidx, line in enumerate(stream):
        if line.lstrip()[0] == '<':
            node_name = line.lstrip()[1:].split(" ")[0].rstrip()
            node = Node(node_name)
            if node_curr:
                node_curr.add_node(node)
            node_curr = node
            line_type = 'TAG_OPEN'
        elif line.lstrip()[0] == '>':
            line_type = 'TAG_CLOSE'
            node_curr = node_curr.prev
        else:
            line_type = 'TAG_INNER'
            node_curr.inner.append(line.strip())
        print(f"[{lidx:4}]: {line.rstrip().ljust(max_line_len)} | {context_msg()}")
