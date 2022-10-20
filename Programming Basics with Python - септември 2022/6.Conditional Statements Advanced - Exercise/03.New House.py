flower = input()
flower_qty = int(input())
budget = int(input())
price = 0

if flower == 'Roses':
    price = 5 * flower_qty
    if flower_qty > 80:
        price *= 0.9
elif flower == 'Dahlias':
    price = 3.80 * flower_qty
    if flower_qty > 90:
        price *= 0.85
elif flower == 'Tulips':
    price = 2.80 * flower_qty
    if flower_qty > 80:
        price *= 0.85
elif flower == 'Narcissus':
    price = 3 * flower_qty
    if flower_qty < 120:
        price *= 1.15
elif flower == 'Gladiolus':
    price = 2.50 * flower_qty
    if flower_qty < 80:
        price *= 1.20

if budget >= price:
    print(f"Hey, you have a great garden with {flower_qty} {flower} and {budget-price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price-budget:.2f} leva more.")

