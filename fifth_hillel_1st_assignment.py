import keyword
import string


def check_variable(name):
    if not name:
        return False

    if name[0] in '0123456789':
        return False

    for symbol in name:
        if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False

    # Rule 3: No spaces or punctuation (except underscore)
    bad_chars = string.punctuation.replace('_', '') + ' '
    for symbol in name:
        if symbol in bad_chars:
            return False

    # Rule 4: Only one underscore allowed
    if name.count('_') > 1:
        return False

    # Rule 5: Can't be a reserved word
    if name in keyword.kwlist:
        return False

    # Only letters, numbers, or underscore allowed
    for symbol in name:
        if not (symbol in 'abcdefghijklmnopqrstuvwxyz0123456789_'):
            return False

    return True


name = input()
print(check_variable(name))