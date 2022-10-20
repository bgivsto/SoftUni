product = input()
city = input()
qty = float(input())

if city == 'Sofia':
    price = 0
    if product == 'coffee':
        price = 0.50
    elif product == 'water':
        price = 0.80
    elif product == 'beer':
        price = 1.20
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60
    print(price * qty)

elif city == 'Plovdiv':
    price = 0
    if product == 'coffee':
        price = 0.40
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50
    print(price * qty)

elif city == 'Varna':
    price = 0
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55
    print(price * qty)
