import factory

from formula import Formula

if __name__ == "__main__":
    text_formula = input('Input formula to eval. \nImplemented operators: {}\n'.format('|'.join([op for op in factory.operators])))
    print(Formula(text_formula).eval())
