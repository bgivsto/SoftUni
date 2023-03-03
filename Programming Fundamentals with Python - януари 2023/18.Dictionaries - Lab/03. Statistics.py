products = {}

while True:
    entry = input()
    if entry == "statistics":
        break
    else:
        key, value = entry.split(": ")
        if key in products:
            products[key] += int(value)
        else:
            products[key] = int(value)

print("Products in stock:")

for k, v in products.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")