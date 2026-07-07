def number_pattern(n):
    if type(n) != int:
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    pattern = ''
    for i in range(1, n):
        pattern += str(i) + ' '
    pattern += str(n)
    return pattern