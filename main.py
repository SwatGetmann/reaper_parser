import datetime
import sys
import argparse
import os

from reaper_project import ReaperProject 

parser = argparse.ArgumentParser(
    description="Reaper Parser utility - parses any given *.rpp file (Reaper DAW)."
)
parser.add_argument('--file_path', 
                    type=lambda p: p if os.path.exists(p) else None,
                    help='path to rpp file to parse'
)

if __name__ == '__main__': 
    print("Welcome to Reaper Parser.")
    
    args = parser.parse_args()
    print(args)
    
    if args.file_path:
        ReaperProject(args.file_path)
    else:
        print("No file path had been given.")
