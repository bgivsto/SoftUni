n = int(input())
capacity = 255
liters = 0

for i in range(n):
    water = int(input())
    if liters + water > capacity:
        print("Insufficient capacity!")
        continue
    else:
        liters += water

print(liters)
