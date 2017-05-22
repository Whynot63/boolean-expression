class FormulaMember:
    #def __str__(self):
    #    return self.symbol

    def eval(self, *args):
        return int(self.truth_table(*[a.eval() for a in args]))


class Atom(FormulaMember):
    def __init__(self, name, value=None):
        self.symbol = name
        self.priority = 0
        self.dim = 0

        if name.isdigit():
            self.truth_table = lambda : int(name)
        else:
            self.truth_table = lambda : value

    def set_value(self, value):
        self.truth_table = lambda : value

    @property
    def value(self):
        return self.truth_table()


class Operator(FormulaMember):
    def __init__(self, symbol, truth_table, dimension, priority):
        self.truth_table = truth_table
        self.dim = dimension
        self.priority = priority
        self.symbol = symbol
