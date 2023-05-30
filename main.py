import re

from typing import AnyStr, List

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
        
        active_block_name = None
        
        notes_block = Notes([])
        
        for line_idx, line in enumerate(lines):
            if re.match(open_block_r, line):
                match = re.search(open_block_r, line)
                # print(line)
                # print(match)
                active_block_name = match.group(1)
                stack.append(active_block_name)
                index_map[active_block_name] = line_idx
                
                if active_block_name == 'NOTES':
                    pass
            elif re.search(end_block_r, line):
                el_tag = stack.pop()
                if stack:
                    active_block_name = stack[-1]
                print("<{}>, {} to {}".format(
                    el_tag, index_map[el_tag], line_idx
                ))
            else:
                # we're inside the block
                if active_block_name == 'NOTES':
                    notes_block.append_line(line)
        
        print(notes_block)
           
    
class Notes:
    """
    Notes block from Reaper Project (*.rpp) files.
    """
    
    def __init__(self, lines: List[AnyStr]) -> None:
        if lines:
            self.lines = lines
        else:
            self.lines = []
    
    def append_line(self, line: AnyStr) -> None:
        self.lines.append(line)
    
    def __str__(self) -> str:
        return "\n".join(self.lines)
                
        

if __name__ == '__main__':
    print("Welcome to Reaper Parser.")
    
    test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\221012 01 Tbilisi Sunrise\\221012 01 Zoom Rec Again.rpp"
    # test_reaper_project_fpath = "d:\\05 Music Lab\\Вдохновения\\Tbilisi Acoustic G\\230503 three ideas\\230503 three ideas.rpp"
        
    ReaperProject(test_reaper_project_fpath)