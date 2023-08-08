import datetime
import sys
import argparse
import os

from reaper_project import ReaperProject
from node_type import NodeType

parser = argparse.ArgumentParser(
    description="Reaper Parser utility - parses any given *.rpp file (Reaper DAW)."
)
parser.add_argument('--file_path', 
                    type=lambda p: p if os.path.exists(p) else None,
                    help='path to rpp file to parse'
)
parser.add_argument('--debug', 
                    type=bool,
                    help='debug mode switch'
)

if __name__ == '__main__': 
    print("Welcome to Reaper Parser.")

    args = parser.parse_args()
    print(args)

    if args.file_path:
        rp = ReaperProject(args.file_path, debug_log=args.debug)
        # rp.head.print_tree()
        fetch_res = rp.head.fetch(NodeType.VST, [])
        for res in fetch_res:
            res.print_tree()
        
        fetch_res = rp.head.fetch(NodeType.NOTES, [])
        for res in fetch_res:
            res.print_tree()
    else:
        print("No file path had been given.")
