import argparse
import os

from tokenizer import tokenize_node

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
        rps = tokenize_node(open(args.file_path, 'r').readlines(), supress_output=args.debug)
        rps[0].print_tree()
        # fetch_res = rp.head.fetch(NodeType.VST, [])
        # for res in fetch_res:
        #     res.print_tree()
        
        # fetch_res = rp.head.fetch(NodeType.NOTES, [])
        # for res in fetch_res:
        #     res.print_tree()
    else:
        print("No file path had been given.")
