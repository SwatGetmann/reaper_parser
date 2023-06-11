from reaper_project import ReaperProject 

import datetime

import sys

if __name__ == '__main__': 
    print("Welcome to Reaper Parser.")
    
    print(sys.argv)
    
    if len(sys.argv) > 1 and sys.argv[1]:
        rpp_path = sys.argv[1]
        print("Processing file: ... {}".format(rpp_path))
        ReaperProject(rpp_path)
