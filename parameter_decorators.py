import re
from typing import Pattern, Optional, Callable
from parameter import Parameter
from parameter_type import ParameterType
from parser_utils import line_param_parsing


def single_line_create_param(
    line: str,
    line_idx: int,
    regexp: Pattern[str],
    type_override: Optional[str] = None,
    debug_log: bool = False
) -> Callable:
    """Generator for single line parameters.

    Args:
        line (str): Line to parse parameters from.
        line_idx (int): Line index.
        regexp (Pattern[str]): Compiled regular expression.
        type_override (str, optional): ParameterType string \
            to override parameter initialization. Defaults to None.
    """
    def create_param(append=None):
        match = re.search(regexp, line)
        match_res = match.group(1)
        if debug_log:
            if match_res != 'E' and match_res != 'e':
                log_msg = f"[Line {line_idx}] :: Param Type Found: {match_res}"
                print(log_msg)
        if type_override:
            param = Parameter(type=type_override)
        else:
            param = Parameter(type=ParameterType[match_res])
        if append:
            append(param, match_res)
        param.lines.append(line.strip())
        values = line_param_parsing(line, match_res, tag=False)
        param.values += values
        return param
    return create_param