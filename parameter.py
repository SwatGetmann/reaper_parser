from parameter_type import ParameterType

import base64

class Parameter:
    def __init__(self, type: ParameterType) -> None:
        self.type = type
        self.lines = []
        self.values = [] # can be list of any type (int,float, str, bytes), depending on type of parameter

    def __str__(self) -> str:
        if self.type == ParameterType.MULTILINE:
            concat = "".join(self.lines[0])
            concat_b64 = base64.b64decode(concat)
            return "{} : {}".format(self.type, concat_b64)
        else:
            return "{} : {}".format(self.type, self.lines)
