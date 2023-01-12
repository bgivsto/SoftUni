orders = int(input())
total_price = 0

for i in range(orders):
    capsule_price = float(input())
    days = int(input())
    daily_capsules = int(input())
    if (0.01 <= capsule_price <= 100.00) and (1 <= days <= 31) and (1 <= daily_capsules <= 2000):
        order_price = capsule_price * daily_capsules * days
        print(f"The price for the coffee is: ${order_price:.2f}")
        total_price += order_price
    else:
        continue

print(f"Total: ${total_price:.2f}")
