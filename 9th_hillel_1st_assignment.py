def popular_words(text, words):
    # Зводимо весь текст до нижнього регістру і розбиваємо на слова
    text = text.lower().split()
    # Повертаємо словник: ключ — шукане слово, значення — кількість входжень у тексті
    return {word: text.count(word) for word in words}


# Перевірка через assert
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}, 'Test1'

print('OK')
