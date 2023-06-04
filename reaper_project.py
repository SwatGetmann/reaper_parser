import re

from node import Node, NodeType
from parameter import Parameter, ParameterType

class ReaperProject:
    """
    Parser for *.rpp Reaper Project files.
    """
   
    def __init__(self, filepath: str) -> None:
       self.filepath = filepath
       self.parse()
    
    def parse(self) -> None:
        with open(self.filepath) as f:  
            lines = f.readlines()
        
        # !TODO: Index Map - what is it for? \
        # * What are the use cases?
        # * Are we planning to use it somehow?
        index_map = {}
        
        stack = []
        
        open_block_r = r"\s*<([A-Z_]+)"
        end_block_r = r"^\s*\>\n"
        
        node_token = None
                
        head = Node(type=NodeType.REAPER_PROJECT)
        prev = None
        
        # TODO! : handle multiline parameters
        multiline_flag = False
        # multiline_param_start_idx = 0
        single_line_param_r = r"\s+([A-Z0-9_]+)\s+"
        
        for line_idx, line in enumerate(lines):
            if re.match(open_block_r, line):
                match = re.search(open_block_r, line)
                
                # print(line)
                # print(match)
                
                node_token = match.group(1)
                stack.append(node_token)
                index_map[node_token] = line_idx
                
                inner_level = len(stack)
                
                # print(inner_level)
                
                if inner_level > 1:
                    prev = head
                    head = Node(type=NodeType[node_token])
                    head.prev = prev
                    head.depth = inner_level - 1
                
                    # process line (header parameters) according to node.type
                
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                inner_level -= 1
                
                # print("Closing block, inner level: {}".format(inner_level))
                # print(inner_level)
                
                if text_param and multiline_flag:
                    head.parameters.append(text_param)
                    text_param = None
                    multiline_flag = False
                
                if inner_level > 0:
                    curr = head
                    head = head.prev
                    prev = head.prev
                    
                    head.inner.append(curr)
                    
                    node_token = stack[-1]

                # print(head)
                    
                print("Level: {} :: <{}>, {} to {}".format(
                    inner_level+1, el_tag, index_map[el_tag], line_idx
                ))
            elif re.search(single_line_param_r, line):
                multiline_flag = False
                param_match = re.search(single_line_param_r, line)
                param_type = param_match.group(1)
                print("[Line {}] :: Param Type Found: {}".format(line_idx, param_type))
                # text_param = Parameter(type=ParameterType[param_type])
                text_param = Parameter(type=ParameterType.TEXT) # for test
                text_param.values.append(line)
                
                head.parameters.append(text_param)
            else:
                if multiline_flag == False:
                    multiline_flag = True
                    # multiline_param_start_idx = line_idx
                    text_param = Parameter(type=ParameterType.TEXT)
                if text_param and multiline_flag:
                    text_param.values.append(line)
                    
        self.print_node_tree(head)
    
    def print_node_tree(self, head: Node):
        print(head)
        for p in head.parameters:
            print(p)
        for n in head.inner:
            print(n)
            for p in n.parameters:
                print(p)
            for n_2 in n.inner:
                print(n_2)
                print(n_2.parameters)