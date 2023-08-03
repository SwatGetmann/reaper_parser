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
        print("Processing file: ... {}".format(self.filepath))
        
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
                
        head = Node(ntype=NodeType.REAPER_PROJECT)
        prev = None
        
        # TODO! : handle multiline parameters
        multiline_flag = False
        single_line_param_r = r"\s+([A-Z0-9_]+)\s+"
        uuid_line_param_r = r"\s+(\{{1}[A-F0-9-]+\}{1})\s+"
        
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
                    head = Node(ntype=NodeType[node_token])
                    head.prev = prev
                    head.depth = inner_level - 1
                
                    # process line (header parameters) according to node.type
                
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                inner_level -= 1
                
                # print("Closing block, inner level: {}".format(inner_level))
                # print(inner_level)
                
                if param and multiline_flag:
                    head.parameters.append(param)
                    param = None
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
            elif multiline_flag == False and re.search(single_line_param_r, line):
                if node_token == 'SWSAUTOCOLOR':
                    print("PEEEP!")
                    print(line)
                    param_match = re.search(uuid_line_param_r, line)
                    id = param_match.group(1)
                    print("[Line {}] :: Param Type Found: {}".format(line_idx, id))                
                    param = Parameter(type=ParameterType.SWSCOLOR_ID)
                    # param = Parameter(type=ParameterType.TEXT) # for test
                    param.values.append({'ID': id})
                    param.values.append(line)
                    
                    head.parameters.append(param)
                else:
                    # multiline_flag = False
                    param_match = re.search(single_line_param_r, line)
                    param_type = param_match.group(1)
                    print("[Line {}] :: Param Type Found: {}".format(line_idx, param_type))                
                    param = Parameter(type=ParameterType[param_type])
                    # param = Parameter(type=ParameterType.TEXT) # for test
                    param.values.append(line)
                    head.parameters.append(param)
            else:
                if multiline_flag == False:
                    multiline_flag = True
                    param = Parameter(type=ParameterType.TEXT)
                if param and multiline_flag:
                    param.values.append(line)
                    
        self.print_node_tree(head)
    
    def print_node_tree(self, head: Node) -> None:
        """Prints node tree, from a given head

        Args:
            head (Node): a node to print (sub-)tree from
        """
        head.print_tree()
