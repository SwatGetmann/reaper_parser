import re

from node import Node, NodeType
from parameter import Parameter, ParameterType


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


    def parse(self) -> None:
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

        # TODO! : handle multiline parameters
        multiline_flag = False

        with open(self.filepath) as f:
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
                    head.parameters_first_line = param_strs

                elif re.search(self.BLOCK_END_RGX, line):
                    el_tag = stack.pop()
                    inner_level -= 1

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

                    level_log_msg = f"L {inner_level+1} :: <{el_tag}>, {index_map[el_tag]} to {line_idx}"
                    print(level_log_msg)
                elif not multiline_flag and re.search(self.PARAM_LINE_SINGLE_RGX, line):
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


def single_line_create_param(line, line_idx, regexp, type_override=None):
    def create_param(append=None):
        match = re.search(regexp, line)
        match_res = match.group(1)
        if match_res != 'E' and match_res != 'e':
            log_msg = f"[Line {line_idx}] :: Param Type Found: {match_res}"
            print(log_msg)
        if type_override:
            param = Parameter(type=type_override)
        else:
            param = Parameter(type=ParameterType[match_res])
        if append:
            append(param, match_res)
        param.values.append(line.strip())
        return param
    return create_param
