import string


class AlgebraSolver:
    def __init__(self, equation: str):
        self.equation = equation
        self.tokens = []
        self.x_val = 0
        self.this_string_to_int = ""
        self.switch_ops = {"+": "-", "-": "+", "*": "/", "/": "*"}

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
        print(self.tokens)

    def get_ops(self):
        pass

    def reverse_ops(self, ops):
        pass


algebra_solver = AlgebraSolver("3*x+1=16")
algebra_solver.get_tokens()
