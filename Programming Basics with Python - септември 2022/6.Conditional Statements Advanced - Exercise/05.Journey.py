budget = float(input())
season = input()
price = 0
destination = ''
vacation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        vacation_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        vacation_type = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        vacation_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        vacation_type = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    price = budget * 0.9
    vacation_type = 'Hotel'


print(f"Somewhere in {destination}")
print(f"{vacation_type} - {price:.2f}")



