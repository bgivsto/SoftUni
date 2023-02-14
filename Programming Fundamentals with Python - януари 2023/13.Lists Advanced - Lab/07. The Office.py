happiness = [int(x) for x in input().split()]
factor = int(input())
new_happiness = [x * factor for x in happiness]
average_happiness = sum(new_happiness) / len(new_happiness)
filtered = list(filter(lambda x: x >= average_happiness, new_happiness))

if len(filtered) >= len(new_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(new_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(new_happiness)}. Employees are not happy!")
