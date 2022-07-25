word = input()

if len(word) == 1 and word.lower() == word:
    print(word.upper())
elif word.upper() == word:
    print(word.lower())
elif word[0].lower() == word[0] and word[1:].upper() == word[1:]:
    print(word[0].upper() + word[1:].lower())
else:
    print(word)
