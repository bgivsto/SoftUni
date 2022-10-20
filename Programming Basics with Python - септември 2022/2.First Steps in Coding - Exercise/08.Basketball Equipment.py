annual_price = int(input())

shoes = annual_price * 0.6
jersey = shoes * 0.8
ball = jersey / 4
acc = ball / 5

total_price = shoes + jersey + ball + acc + annual_price

print(total_price)