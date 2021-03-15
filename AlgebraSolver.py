import string


class AlgebraSolver:
    def __init__(self, equation: str):
        self.equation = equation
        self.tokens = []
        self.x_val = 0

    def get_tokens(self):
        self.tokens = []
        for char in self.equation:
            this_string_to_int = ""
            if char not in string.digits:
                pass
            elif char == " ":
                pass
            else:
                this_string_to_int += char
        print(self.tokens)


AlgebraSolver("3x+1=16")
