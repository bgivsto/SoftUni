n = int(input())

first_half = 0
second_half = 0
for i in range(2*n):
    num = int(input())
    if i < n:
        first_half += num
    else:
        second_half += num

if first_half == second_half:
    print(f"Yes, sum = {first_half}")
else:
    print(f"No, diff = {abs(first_half-second_half)}")


