import re

from members import Operator, Atom


variables = dict()
operators = {
    'NOT' : Operator(
        symbol='NOT',
        truth_table=lambda x1: not x1,
        dimension=1,
        priority=1),

    'XOR' : Operator(
        symbol='XOR',
        truth_table=lambda x1, x2:  (x1 or x2) and not (x1 and x2),
        dimension=2,
        priority=2),

    '->' : Operator(
        symbol='->',
        truth_table=lambda x1, x2: not (x1 and not x2),
        dimension=2,
        priority=2),

    'AND' : Operator(
        symbol='AND',
        truth_table=lambda x1, x2: x1 and x2,
        dimension=2,
        priority=3),

    'OR' : Operator(
        symbol='OR',
        truth_table=lambda x1, x2: x1 or x2,
        dimension=2,
        priority=4),
}

#TODO implement regex to atom and operators search
atom_pattern = re.compile('^([a-zA-Z0-9]+)\s?(?={}|$)'.format(''.join(['\('] + ['|' + op for op in operators])))
operators_seq = '|'.join([op for op in operators])
#operator_pattern = re.compile('^({})'.format(operators_seq)))


def get_object(string):
    if string.startswith('AND'):
        return operators['AND'], 3
    elif string.startswith('OR'):
        return operators['OR'], 2
    elif string.startswith('NOT'):
        return operators['NOT'], 3
    elif string.startswith('XOR'):
        return operators['XOR'], 3
    elif string.startswith('->'):
        return operators['->'], 2
    else:
        symbol = string.split()[0]
        if symbol not in variables:
            variables[symbol] = Atom(symbol)
        return variables[symbol], len(symbol)
