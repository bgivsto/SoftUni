change = round(float(input()) * 100)
coins = 0

while change:
    coins += 1
    if change >= 200:
        change -= 200
    elif 100 <= change < 200:
        change -= 100
    elif 50 <= change < 100:
        change -= 50
    elif 20 <= change < 50:
        change -= 20
    elif 10 <= change < 20:
        change -= 10
    elif 5 <= change < 10:
        change -= 5
    elif 2 <= change < 5:
        change -= 2
    elif change < 2:
        change -= 1

print(coins)
