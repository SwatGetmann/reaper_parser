import re

from node import Node, NodeType

class ReaperProject:
    """
    Parser for *.rpp Reaper Project files.
    """
   
    def __init__(self, filepath: str) -> None:
       self.filepath = filepath
       self.parse()
    
    def parse(self) -> None:
        lines = open(self.filepath).readlines()
        index_map = {}
        stack = []
        
        open_block_r = r"\s*<([A-Z_]+)"
        end_block_r = r"^\s*\>\n"
        
        node_type_name = None
        
        # notes_block = Node(type=NodeType.NOTES)
        
        head = Node(type=NodeType.REAPER_PROJECT)
        prev = None
        
        for line_idx, line in enumerate(lines):
            if re.match(open_block_r, line):
                match = re.search(open_block_r, line)
                
                # print(line)
                # print(match)
                
                node_type_name = match.group(1)
                stack.append(node_type_name)
                index_map[node_type_name] = line_idx
                
                inner_level = len(stack)
                
                # print(inner_level)
                
                if inner_level > 1:
                    prev = head
                    head = Node(type=NodeType[node_type_name])
                    head.prev = prev
                    head.depth = inner_level - 1
                    print(head)
                
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                inner_level -= 1
                
                # print("Closing block, inner level: {}".format(inner_level))
                # print(inner_level)
                
                if inner_level > 0:
                    curr = head
                    curr.max_depth = inner_level
                    
                    head = head.prev
                    prev = head.prev
                    
                    head.inner.append(curr)
                    # print("HEAD M/: {}, CURR M/: {}".format(head.max_depth, curr.max_depth))
                    head.max_depth = max(head.max_depth, curr.max_depth)
                    # if prev:
                        # prev.max_depth = max(prev.max_depth, head.max_depth + 1)
                    
                    node_type_name = stack[-1]

                # print(head)
                    
                print("Level: {} :: <{}>, {} to {}".format(
                    inner_level+1, el_tag, index_map[el_tag], line_idx
                ))
            # else:
                # we're inside the block
                # if node_type_name == 'NOTES':
                #     notes_block.parameters.append(line)
        
        print(head)
        for n in head.inner:
            print(n)
            for n_2 in n.inner:
                print(n_2)
    