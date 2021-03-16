import string


class AlgebraSolver:
    def __init__(self, equation: str):
        self.equation = equation
        self.tokens = []
        self.x_val = 0
        self.this_string_to_int = ""
        self.ops_order = []
        self.reverse_ops_dict = {"+": "-", "-": "+", "*": "/", "/": "*"}  # TODO: Add support for situations like 3x=3*x
        self.sort_key = {"+": 0, "-": 1, "*": 2, "/": 3}  # used for sorting the reverse order of operations

    def get_tokens(self):
        self.tokens = []
        for char in self.equation:
            if char not in string.digits:
                if not self.this_string_to_int == "":
                    self.tokens.append(int(self.this_string_to_int))
                    self.this_string_to_int = ""
                self.tokens.append(char)
            elif char == " ":
                pass
            else:
                self.this_string_to_int += char
        if not self.this_string_to_int == "":
            self.tokens.append(int(self.this_string_to_int))
            self.this_string_to_int = ""

    def do_ops(self):
        self.x_val = self.tokens.pop(-1)  # Set initial x_val
        self.tokens.pop(-1)  # TODO: Add support for things like 1+x = 5*3+1; I intend for it to solve the right side
                             #   then solve the left like normal
        self.ops_order = self.prepare_ops()
        print(self.ops_order)

    def prepare_ops(self):
        reversed_ops = []
        for token in self.tokens:
            if token in self.reverse_ops_dict.keys():
                reversed_ops.append(self.reverse_ops_dict[token])
        reversed_ops = list(sorted(zip(reversed_ops, [self.sort_key[i] for i in reversed_ops]), key=lambda item: item[1]))
        return reversed_ops


algebra_solver = AlgebraSolver("3*x+1=16")
algebra_solver.get_tokens()
algebra_solver.do_ops()
