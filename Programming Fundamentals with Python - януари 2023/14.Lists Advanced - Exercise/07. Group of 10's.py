from math import ceil

numbers = [int(x) for x in input().split(", ")]
groups = ceil(max(numbers) / 10)

for i in range(1, groups + 1):
    group = list(filter(lambda x: x <= i*10, numbers))
    for element in group:
        numbers.remove(element)
    print(f"Group of {i*10}'s: {group}")

