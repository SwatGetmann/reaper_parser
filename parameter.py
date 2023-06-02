from parameter_type import ParameterType

class Parameter:
    def __init__(self, type: ParameterType) -> None:
        self.type = type
        self.values = [] # can be list of any type (int,float, str, bytes), depending on type of parameter