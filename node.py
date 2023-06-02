from node_type import NodeType

class Node:
    def __init__(self, type: NodeType) -> None:
        self.type = type
        self.inner = []         # list of Nodes
        self.prev = None
        self.parameters = []    # list of Parameters
        self.depth = 0          # 0 = head, maximal value = distance of leaf
        # self.max_depth = 0
    
    def __str__(self) -> str:       
        return "{} -> {}.[{} /{}]".format(self.prev, self.type, len(self.inner), self.depth)


        