products = {}

while True:
    line = input()
    if line == "buy":
        break

    name = line.split()[0]
    price = float(line.split()[1])
    qty = int(line.split()[2])

    if name not in products:
        products[name] = [price, qty]
    else:
        products[name][0] = price
        products[name][1] += qty

for k, v in products.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")