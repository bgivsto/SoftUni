text = input()
result = ""
for letter in text:
    result += chr(ord(letter) + 3)

print(result)