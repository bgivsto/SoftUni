budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == 'Spring':
    price = 3000
    if 0 < fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
    if fishermen % 2 == 0:
        price *= 0.95
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if 0 < fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
    if season == 'Summer' and fishermen % 2 == 0:
        price *= 0.95
elif season == 'Winter':
    price = 2600
    if 0 < fishermen <= 6:
        price *= 0.9
    elif 7 <= fishermen <= 11:
        price *= 0.85
    elif fishermen >= 12:
        price *= 0.75
    if fishermen % 2 == 0:
        price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget-price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price-budget:.2f} leva.")
