n = int(input())
word = input()
lst = []

for i in range(n):
    entry = input()
    lst.append(entry)

print(lst)
result = [x for x in lst if word in x]
print(result)