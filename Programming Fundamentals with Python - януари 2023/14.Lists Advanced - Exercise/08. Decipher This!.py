message = input().split()

for word in message:
    number = ""
    for letter in word:
        if letter.isdigit():
            number += letter
            word = word.replace(letter, "")
    word = chr(int(number)) + word
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    print("".join(word), end=" ")

