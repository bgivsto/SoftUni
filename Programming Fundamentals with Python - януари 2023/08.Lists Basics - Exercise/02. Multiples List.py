factor = int(input())
count = int(input())

result = [x for x in range(factor, count * factor + 1) if x % factor == 0]
print(result)
