items = input().split("|")
initial_budget = float(input())
budget = initial_budget
new_prices = []

for item in items:
    if budget < 0:
        break

    item_type, price = item.split("->")[0], float(item.split("->")[1])

    if price <= budget:
        if item_type == "Clothes" and price <= 50.00:
            new_prices.append(price * 1.4)
            budget -= price
        elif item_type == "Shoes" and price <= 35.00:
            new_prices.append(price * 1.4)
            budget -= price
        elif item_type == "Accessories" and price <= 20.50:
            new_prices.append(price * 1.4)
            budget -= price

print(" ".join([str(f'{price:.2f}') for price in new_prices]))
new_budget = budget + sum(new_prices)
print(f"Profit: {new_budget - initial_budget:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
