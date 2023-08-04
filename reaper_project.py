import re

from node import Node, NodeType
from parameter import Parameter, ParameterType


class ReaperProject:
    """
    Parser for *.rpp Reaper Project files.
    """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.head = self.parse()
        self.head.print_tree()


    def parse(self) -> None:
        print(f"Processing file: ... {self.filepath}")

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

                level_log_msg = f"L {inner_level+1} :: <{el_tag}>, {index_map[el_tag]} to {line_idx}"
                print(level_log_msg)
            elif not multiline_flag and re.search(single_line_param_r, line):
                if node_token == 'SWSAUTOCOLOR':
                    get_param = single_line_create_param(
                        line, 
                        line_idx, 
                        uuid_line_param_r,
                        ParameterType.SWSCOLOR_ID
                    )
                    param = get_param(lambda p, m: p.values.append({'ID': m}))
                    head.parameters.append(param)
                else:
                    get_param = single_line_create_param(
                        line, 
                        line_idx, 
                        single_line_param_r
                    )
                    param = get_param()
                    head.parameters.append(param)
            else:
                if not multiline_flag:
                    multiline_flag = True
                    param = Parameter(type=ParameterType.TEXT)
                if param and multiline_flag:
                    param.values.append(line)

        return head


def single_line_create_param(line, line_idx, regexp, type_override=None):
    def create_param(append=None):
        match = re.search(regexp, line)
        match_res = match.group(1)
        log_msg = f"[Line {line_idx}] :: Param Type Found: {match_res}"
        print(log_msg)
        if type_override:
            param = Parameter(type=type_override)
        else:
            param = Parameter(type=ParameterType[match_res])
        if append:
            append(param, match_res)
        param.values.append(line)
        return param
    return create_param
