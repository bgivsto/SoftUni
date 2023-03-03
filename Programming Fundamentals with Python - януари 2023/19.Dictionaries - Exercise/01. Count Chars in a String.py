text = input()

result = {}
for letter in text:
    if letter != " ":
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1

for k, v in result.items():
    print(f"{k} -> {v}")
