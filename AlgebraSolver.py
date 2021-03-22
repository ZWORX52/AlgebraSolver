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
        self.start()

    def get_tokens(self):
        self.tokens = []
        for char in self.equation:
            if char not in string.digits + ".":
                if not self.this_string_to_int == "":
                    self.tokens.append(float(self.this_string_to_int))
                    self.this_string_to_int = ""
                self.tokens.append(char)
            elif char == " ":
                pass
            else:
                self.this_string_to_int += char
        if not self.this_string_to_int == "":
            self.tokens.append(float(self.this_string_to_int))
            self.this_string_to_int = ""

    def do_ops(self):
        self.x_val = self.tokens.pop(-1)  # Set initial x_val
        self.tokens.pop(-1)  # TODO: Add support for things like 1+x = 5*3+1; I intend for it to solve the right side
                             #   then solve the left like normal
        self.ops_order = [item[0] for item in self.prepare_ops()]
        for op in self.ops_order:
            self.x_val = eval("self.x_val" + op[0] + str(op[1]))
        print(self.x_val)

    def prepare_ops(self):
        reversed_ops = []
        for token in range(len(self.tokens)):
            if self.tokens[token] in self.reverse_ops_dict.keys():
                reversed_ops.append((self.reverse_ops_dict[self.tokens.pop(token)], self.tokens.pop(token + 1)))
        return list(sorted(zip(reversed_ops, [self.sort_key[i] for i in [i[0] for i in reversed_ops]]),
                           key=lambda item: item[0]))

    def start(self):
        self.get_tokens()
        self.do_ops()


while True:
    AlgebraSolver(input("Equation: "))
