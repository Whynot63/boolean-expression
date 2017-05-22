from __future__ import print_function

tests = [
    ['0', 0],
    ['1', 1],
    ['NOT 0', 1],
    ['NOT 1', 0],

    ['0 AND 0', 0],
    ['0 AND 1', 0],
    ['1 AND 0', 0],
    ['1 AND 1', 1],

    ['0 OR 0', 0],
    ['0 OR 1', 1],
    ['1 OR 0', 1],
    ['1 OR 1', 1],

    ['1 AND (NOT 0 OR 0)', 1],
    ['0 AND (NOT 0 OR 0)', 0],

    ['(0 OR (NOT 1 AND 0)) AND (NOT 0 OR 0)', 0],
    ['(0 OR NOT (1 AND 0)) AND (NOT 0 OR 0)', 1],

    ['NOT 0 OR (NOT 0 OR 0)', 1],
]

from formula import Formula

if __name__ == "__main__":
    for i, test in enumerate(tests):
        problem, answer = test

        f = Formula(problem)
        assert f.eval() == answer
        print('{}/{} passed...'.format(i + 1, len(tests)))
