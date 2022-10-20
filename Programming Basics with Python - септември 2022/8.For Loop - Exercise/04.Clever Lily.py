age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

current_birthday_money = 0
toys = 0
total_money = 0
taken_money = 0

for i in range(1, age+1):
    if i % 2 == 0:
        current_birthday_money += 10
        taken_money += 1
        total_money += current_birthday_money
    else:
        toys += 1

total_money = total_money + toys * toy_price - taken_money

if total_money >= washing_machine_price:
    print(f"Yes! {total_money-washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price-total_money:.2f}")
