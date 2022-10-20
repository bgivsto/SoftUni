needed_money = float(input())
available_money = float(input())
spending_days = 0
total_days = 0
success = True

while available_money < needed_money:
    act = input()
    money = float(input())
    total_days += 1
    if act == 'spend':
        available_money -= money
        spending_days += 1
        if available_money < 0:
            available_money = 0
        if spending_days == 5:
            success = False
            print("You can't save the money.")
            print(total_days)
            break
    elif act == 'save':
        available_money += money
        spending_days = 0

if success:
    print(f"You saved the money for {total_days} days.")
