budget = float(input())
videocards_qty = int(input())
processors_qty = int(input())
ram_qty = int(input())

videocard_price = 250
processor_price = videocard_price * videocards_qty * 0.35
ram_price = videocard_price * videocards_qty * 0.1

total_price = videocard_price * videocards_qty + processor_price * processors_qty + ram_price * ram_qty

if videocards_qty > processors_qty:
    total_price = total_price - total_price * 0.15

if budget >= total_price:
    print(f'You have {budget-total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price-budget:.2f} leva more!')