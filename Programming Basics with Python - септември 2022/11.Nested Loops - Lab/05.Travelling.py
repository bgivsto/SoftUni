available_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while available_money < budget:
        available_money += float(input())
    print(f"Going to {destination}!")
    available_money = 0
