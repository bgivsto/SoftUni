first_strings = input().split(", ")
second_strings = input().split(", ")

result = []

for word1 in first_strings:
    for word2 in second_strings:
        if word1 in word2:
            result.append(word1)
            break

print(result)

