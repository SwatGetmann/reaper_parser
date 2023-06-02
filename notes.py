from typing import List

class Notes:
    """
    Legacy/draft stuff 
    -- implementation of Notes, that should be done as ENUM instead.
    """
    
    def __init__(self, lines: List[str]) -> None:
        if lines:
            self.lines = lines
        else:
            self.lines = []
    
    def append_line(self, line: str) -> None:
        self.lines.append(line)
    
    def __str__(self) -> str:
        return "\n".join(self.lines)
