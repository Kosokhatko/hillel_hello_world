import keyword
import string


def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False

    if name.count('_') > 1:
        return False

    if len(name) == 0 or name[0].isdigit():
        return False

    allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    for ch in name:

        if ch not in allowed_chars:
            return False

    return True


test_cases = [
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception",
]

for test in test_cases:
    print(is_valid_variable_name(test))





