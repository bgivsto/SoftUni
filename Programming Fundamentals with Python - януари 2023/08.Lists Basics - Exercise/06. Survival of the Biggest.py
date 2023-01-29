lst = [int(x) for x in input().split(" ")]
n = int(input())

for i in range(n):
    lst.remove(min(lst))

print(", ".join([str(x) for x in lst]))
