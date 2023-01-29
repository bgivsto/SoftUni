lst = [int(x) for x in input().split(", ")]

for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))

print(lst)