import factory

from formula import Formula

if __name__ == "__main__":
    text_formula = input('Input formula to eval. \nImplemented operators: {}\n'.format('|'.join([op for op in factory.operators])))
    formula = Formula(text_formula)
    truth_table = formula.truth_table

    for variables, answer in truth_table:
        print(' '.join([str(v) for v in variables]) + ' | ' + str(answer))
