words = [word.lower() for word in input().split()]
counted = {word: words.count(word) for word in words}

result = []
for k, v in counted.items():
    if v % 2 != 0:
        result.append(k)

print(" ".join(result))
