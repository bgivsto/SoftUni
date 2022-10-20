movie_type = input()
rows = int(input())
columns = int(input())
price = 0

if movie_type == 'Premiere':
    price = 12.00
elif movie_type == 'Normal':
    price = 7.50
elif movie_type == 'Discount':
    price = 5.00

total_people = rows * columns

total_income = total_people * price

print(f"{total_income:.2f} leva")