def find_close_bracket(string, index_l):
    """Find pare for start bracket
    :param string: sting with brackets
    :param index: index of start bracket
    :return: index of end bracket
    Example:
    find_close_bracket('string(string)', 6) -> 13
    find_close_bracket('string(string)', 0) -> -1
    find_close_bracket('string(str(ing)', 6) -> SyntaxError
    find_close_bracket('string(string))', 6) -> SyntaxError
    """
    counter = 0
    index_r = -1

    for i in range(index_l, len(string)):
        if string[i] == '(':
            counter += 1
        elif string[i] == ')':
            counter -= 1
        if counter == 0 and index_r == -1:
            index_r = i
        if counter < 0:
            raise SyntaxError('Unnecessary end bracket',) #{'text': string, 'offset' : 0})

    if counter != 0:
        raise SyntaxError('Unnecessary start bracket',) #{'text': string, 'offset' : 0})

    return index_r
