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

    bad_chars = string.punctuation.replace('_', '') + ' '
    for symbol in name:
        if symbol in bad_chars:
            return False

    if name.count('_') > 1:
        return False

    if name in keyword.kwlist:
        return False

    for symbol in name:
        if not (symbol in 'abcdefghijklmnopqrstuvwxyz0123456789_'):
            return False

    return True


name = input()
print(check_variable(name))