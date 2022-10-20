text = input()

mapper = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
    }

result = 0
for e in text:
    if e in mapper:
        result += mapper[e]

print(result)