n = int(input())

for num in range(1, n+1):
    sum = 0
    for char in str(num):
        sum += int(char)
    is_special = False
    if sum == 5 or sum == 7 or sum == 11:
        is_special = True
    print(f"{num} -> {is_special}")
