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
]

examples = [
    #'(a OR b AND (NOT c OR a)) AND (b OR NOT c)'
    'NOT b OR (NOT a OR b)'
]

from formula import Formula

if __name__ == "__main__":
    for test in tests:
        problem, answer = test

        f = Formula(problem)
        print('{} -> {}'.format(problem, f))

        template = '{:%dd} -> {:<%dd}' % (len(problem), len(str(f)))
        print(template.format(answer, f.eval()), end='\n\n')
        assert f.eval() == answer

    for example in examples:
        f = Formula(example)
        print(list(map(str, f.polish_notation)))
        print('{} = {}'.format(example, f.eval()))
