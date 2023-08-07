import re
from typing import List
from node import Node, NodeType
from parameter import Parameter, ParameterType
from parameter_decorators import single_line_create_param

class ReaperProject:
    """
    Parser for *.rpp Reaper Project files.
    """

    BLOCK_OPEN_RGX = r"\s*<([A-Z_]+)"
    BLOCK_END_RGX = r"^\s*\>\n"

    PARAM_LINE_SINGLE_RGX = r"\s+([A-Ze0-9_]+)\s+"
    PARAM_LINE_UUID_RGX = r"\s+(\{{1}[A-F0-9-]+\}{1})\s+"

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.head = self.parse()
        # self.head.print_tree()


    def parse(self) -> Node:
        """Parsing of the node tree from RPP file.

        1. Reading the file.
        2. Parsing it line by line.
        3. Storing the parsed data in Node type

        Returns:
            Node: head of the tree
        """
        print(f"Processing file: ... {self.filepath}")

        index_map = {}
        stack = []

        node_token = None
        param = None

        head = Node(ntype=NodeType.REAPER_PROJECT)
        prev = None

        multiline_flag = False

        with open(self.filepath, 'r') as f:
            for line_idx, line in enumerate(f):
                if re.match(self.BLOCK_OPEN_RGX, line):
                    match = re.search(self.BLOCK_OPEN_RGX, line)

                    node_token = match.group(1)
                    stack.append(node_token)
                    index_map[node_token] = line_idx

                    inner_level = len(stack)

                    if inner_level > 1:
                        prev = head
                        head = Node(ntype=NodeType[node_token])
                        head.prev = prev
                        head.depth = inner_level - 1

                    # process line (header parameters) according to node.type
                    param_strs = line_param_parsing(line, node_token)
                    head.parameters_first_line = param_strs

                elif re.search(self.BLOCK_END_RGX, line):
                    closed_node_token = stack.pop()
                    inner_level -= 1

                    if param and multiline_flag:
                        # Stop collecting multiline params
                        # TODO : join lines ?
                        # TODO (?) : change aabstraction to first line, NEXT LINES, parse based by type WHEN NEEDED, lazy style
                        head.parameters.append(param)
                        param = None
                        multiline_flag = False

                    if inner_level > 0:
                        curr = head
                        head = head.prev
                        prev = head.prev
                        head.inner.append(curr)
                        node_token = stack[-1]

                    level_log_msg = f"L {inner_level+1} :: <{closed_node_token}>, {index_map[closed_node_token]} to {line_idx}"
                    print(level_log_msg)
                elif not multiline_flag and re.search(self.PARAM_LINE_SINGLE_RGX, line):
                    # TODO: actually, we can use #line_param_parsing on sinlge lines to get param values instead of archiving the full string
                    if node_token == 'SWSAUTOCOLOR':
                        get_param = single_line_create_param(
                            line,
                            line_idx,
                            self.PARAM_LINE_UUID_RGX,
                            ParameterType.SWSCOLOR_ID
                        )
                        param = get_param(lambda p, m: p.values.append({'ID': m}))
                        head.parameters.append(param)
                    else:
                        get_param = single_line_create_param(
                            line,
                            line_idx,
                            self.PARAM_LINE_SINGLE_RGX
                        )
                        param = get_param()
                        head.parameters.append(param)
                else:
                    if not multiline_flag:
                        multiline_flag = True
                        param = Parameter(type=ParameterType.TEXT)
                    if param and multiline_flag:
                        param.values.append(line.strip())

        return head


def line_param_parsing(line: str, node_token: str) -> List[str]:
    print(line)
    line_split = line.split(f"<{node_token}")
    line_params_str = line_split[1].strip()

    line_str_stack = []
    param_strs = []
    l_pos = 0
    r_pos = 0
    for ci, c in enumerate(line_params_str):
        if c == '"':
            if len(line_str_stack) > 0:
                r_pos = ci
                line_str_stack.pop()
                # print(f"FOUND A SS: {ci} :: {c} :: L {l_pos} , R {r_pos} ;; {line_params_str[l_pos:r_pos]}")
                param_strs.append(line_params_str[l_pos:r_pos])
                l_pos = ci+1
                r_pos = ci+1
            else:
                l_pos = ci+1
                r_pos = ci+1
                line_str_stack.append(c)
        elif c == " ":
            if len(line_str_stack) > 0:
                r_pos += 1
            elif len(line_str_stack) == 0:
                if l_pos < r_pos:
                    # print(f"FOUND A WORD :: L {l_pos} , R {r_pos} ;; {line_params_str[l_pos:r_pos]}")
                    param_strs.append(line_params_str[l_pos:r_pos])
                l_pos = ci+1
                r_pos = ci+1
        else:
            r_pos += 1
        # print(f"{ci} :: {c} :: L {l_pos} , R {r_pos} ;; {line_params_str[l_pos:r_pos]}")
    # dirty hack, but leave for now
    if len(line_params_str) > 0 and len(param_strs) == 0:
        param_strs.append(line_params_str)
    print(param_strs)
    return param_strs
