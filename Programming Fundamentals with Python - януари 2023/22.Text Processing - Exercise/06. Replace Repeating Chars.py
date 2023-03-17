text = input()

result = text[0]

for i in range(len(text)):
    if text[i] != result[-1]:
        result += text[i]

print(result)