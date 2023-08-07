from typing import List

def line_param_parsing(line: str, node_token: str, tag: bool = True) -> List[str]:
    print(line)
    if tag:
        line_split = line.split(f"<{node_token}")
    else:
        line_split = line.split(node_token)
    line_params_str = line_split[1].strip()

    line_str_stack = []
    param_strs = []
    l_pos = 0
    r_pos = 0
    
    len_str = len(line_params_str) - 1
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
            if ci == len_str:
                param_strs.append(line_params_str[l_pos:r_pos])
        # print(f"{ci} :: {c} :: L {l_pos} , R {r_pos} ;; {line_params_str[l_pos:r_pos]}")
    # dirty hack, but leave for now
    if len(line_params_str) > 0 and len(param_strs) == 0:
        param_strs.append(line_params_str)
    print(param_strs)
    return param_strs
