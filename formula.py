import itertools

import util
import factory


class Formula:
    variables = dict()

    def __init__(self, string):
        self.priority = 0
        self.dim = 0

        formula = []
        string = string.strip()
        while len(string) != 0:
            if string[0] != '(':
                member, i = factory.get_object(string)
                formula.append(member)
            else:
                i = util.find_close_bracket(string, 0) + 1
                formula.append(Formula(string[1:i-1]))
            string = string[i:].strip()

        self.formula = formula

        #TODO: use list of member instead Formula class in case with brackets
        if not hasattr(self, 'polish_notation'):
            #TODO: simplify search
            priorities = [m.priority for m in formula]
            i = [i for i, p in enumerate(priorities) if p == max(priorities)][0]

            #TODO мake independent of dim (if possible)
            if formula[i].dim < 2:
                self.polish_notation = formula[i: i + formula[i].dim + 1]

            elif formula[i].dim == 2:
                x1 = formula[i-1] if len(formula[:i]) == 1 else Formula(' '.join(str(m) for m in formula[:i]))
                x2 = formula[i+1] if len(formula[i+1:]) == 1 else Formula(' '.join(str(m) for m in formula[i+1:]))
                self.polish_notation = [formula[i], x1, x2]

            else:
                raise NotImplementedError

    def eval(self):
        return int(self.polish_notation[0].eval(*self.polish_notation[1:]))

    @property
    def truth_table(self):
        variations = itertools.product([0, 1], repeat=len(factory.variables))
        truth_table = []

        for variable in variations:
            for var, value in zip(factory.variables, variable):
                factory.variables[var].set_value(value)
            truth_table.append([variable, self.eval()])
        return truth_table

    def __str__(self):
        return "({})".format(' '.join([str(member) for member in self.formula]))
