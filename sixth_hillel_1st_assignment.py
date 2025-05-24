import string

def get_letter_range(input_str):
    letters = string.ascii_letters
    start, end = input_str.split('-')
    start_idx = letters.index(start)
    end_idx = letters.index(end)
    return letters[start_idx:end_idx + 1]

print(get_letter_range("a-c"))
print(get_letter_range("a-a"))
print(get_letter_range("s-H"))
print(get_letter_range("a-A"))
