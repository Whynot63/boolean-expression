import factory

from formula import Formula

if __name__ == "__main__":
    text_formula = input('Input formula to eval. \nImplemented operators: {}\n'.format(factory.operators_seq))
    print(Formula(text_formula).eval())
