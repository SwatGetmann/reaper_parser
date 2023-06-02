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
        
        active_block_name = None
        
        notes_block = Node(type=NodeType.NOTES)
        
        # head = Node(type=NodeType.REAPER_PROJECT)
        
        for line_idx, line in enumerate(lines):
            if re.match(open_block_r, line):
                match = re.search(open_block_r, line)
                # print(line)
                # print(match)
                active_block_name = match.group(1)
                stack.append(active_block_name)
                index_map[active_block_name] = line_idx
                
                inner_level = len(stack)
                
                if active_block_name == 'NOTES':
                    pass
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                inner_level -= 1
                if stack:
                    active_block_name = stack[-1]
                print("Level: {} :: <{}>, {} to {}".format(
                    inner_level+1, el_tag, index_map[el_tag], line_idx
                ))
            else:
                # we're inside the block
                if active_block_name == 'NOTES':
                    notes_block.parameters.append(line)
        
        print(notes_block)
           
    