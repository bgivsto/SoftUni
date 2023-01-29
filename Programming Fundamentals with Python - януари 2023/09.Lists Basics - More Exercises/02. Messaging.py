indices = input().split(" ")
text = input()

numbers = []
for string in indices:
    value = 0
    for element in string:
        value += int(element)
    numbers.append(value)

word = ""
for number in numbers:
    index = number % len(text)
    word += text[index]
    text = text.replace(text[index], "", 1)

print(word)