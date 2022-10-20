import sys

n = int(input())

max_n = -sys.maxsize
min_n = sys.maxsize

for _ in range(n):
    num = int(input())
    if num < min_n:
        min_n = num
    if num > max_n:
        max_n = num

print(f"Max number: {max_n}")
print(f"Min number: {min_n}")