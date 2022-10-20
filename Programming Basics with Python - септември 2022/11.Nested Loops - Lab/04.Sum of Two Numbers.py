start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
found = False

for n1 in range(start, end+1):
    for n2 in range(start, end+1):
        counter += 1
        if not found and n1 + n2 == magic_number:
            found = True
            print(f"Combination N:{counter} ({n1} + {n2} = {magic_number})")


if not found:
    print(f"{counter} combinations - neither equals {magic_number}")