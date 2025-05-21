import string

def to_hashtag(text: str) -> str:
    cleaned_text = ""
    for symbol in text:
        if symbol not in string.punctuation:
            cleaned_text += symbol

    words = cleaned_text.split()

    capitalized_words = []
    for word in words:
        if len(word) > 0:
            first_letter = word[0].upper()
            rest_of_word = word[1:]
            capitalized_word = first_letter + rest_of_word
            capitalized_words.append(capitalized_word)

    hashtag = "#"
    for word in capitalized_words:
        hashtag += word

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(to_hashtag('Python Community'))
print(to_hashtag('i like python community!'))
print(to_hashtag('Should, I. subscribe? Yes!'))
print(to_hashtag(''))











