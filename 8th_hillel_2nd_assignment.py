def is_palindrome(*texts) -> list[bool]:
    check = lambda text: (clean := ''.join(ch.lower() for ch in text if ch.isalnum())) == clean[::-1]
    return [check(text) for text in texts]

# Тести:
assert is_palindrome('A man, a plan, a canal: Panama')[0] == True, 'Test1'
assert is_palindrome('0P')[0] == False, 'Test2'
assert is_palindrome('a.')[0] == True, 'Test3'
assert is_palindrome('aurora')[0] == False, 'Test4'
print("is_palindrome → OK")
