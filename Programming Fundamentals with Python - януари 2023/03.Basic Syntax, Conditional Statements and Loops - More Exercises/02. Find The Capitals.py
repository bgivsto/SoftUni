word = input()

print([index for index, letter in enumerate(word) if letter.isupper()])

