food = input().split()
bakery = {}

for i in range(0, len(food), 2):
    bakery[food[i]] = int(food[i+1])

print(bakery)
