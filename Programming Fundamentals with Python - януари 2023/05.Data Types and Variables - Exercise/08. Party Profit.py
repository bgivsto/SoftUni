group = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):
    coins += 50
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5
        coins -= group * 2
    if day % 3 == 0:
        coins -= group * 3
    if day % 5 == 0:
        coins += group * 20
    coins -= group * 2

coins_per_member = coins // group
print(f"{group} companions received {coins_per_member} coins each.")
