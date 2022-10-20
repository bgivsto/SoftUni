import sys
n = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    total_sum += number

sum_minus_max = total_sum - max_number

if sum_minus_max == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(sum_minus_max-max_number)}')