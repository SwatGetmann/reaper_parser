from node_type import NodeType

class Node:
    def __init__(self, type: NodeType) -> None:
        self.type = type
        self.inner_elements = [] # list of Nodes
        self.parameters = [] # list of Parameters
    
    def __str__(self) -> str:
        type_str = "> TYPE: {}".format(self.type)
        parameters_str = "> PARAMS: {}".format(self.parameters)
        inner_elements_str = "> * -- {}".format(self.inner_elements)
        
        return "\n".join([type_str, parameters_str, inner_elements_str])
        
        