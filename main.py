import re

from typing import AnyStr

class ReaperProject:
    """
    Parser for *.rpp Reaper Project files.
    """
   
    def __init__(self, filepath: AnyStr) -> None:
       self.filepath = filepath
       self.parse()
    
    def parse(self) -> None:
        lines = open(self.filepath).readlines()
        index_map = {}
        stack = []
        
        open_block_r = r"\s*<([A-Z_]+)"
        end_block_r = r"^\s*\>\n"
        
        for line_idx, line in enumerate(lines):
            if re.match(open_block_r, line):
                match = re.search(open_block_r, line)
                # print(line)
                # print(match)
                stack.append(match.group(1))
                index_map[match.group(1)] = line_idx
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                print("<{}>, {} to {}".format(
                    el_tag, index_map[el_tag], line_idx
                ))
                
                
        

if __name__ == '__main__':
    print("Welcome to Reaper Parser.")
    
    test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\221012 01 Tbilisi Sunrise\\221012 01 Zoom Rec Again.rpp"
        
    ReaperProject(test_reaper_project_fpath)