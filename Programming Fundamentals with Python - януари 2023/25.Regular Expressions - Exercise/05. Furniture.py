import re

pattern = r"^>>(?P<item>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<qty>\d+)"
items = []
price = 0
while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)

    if match:
        data = match.groupdict()
        items.append(data['item'])
        price += float(data['price']) * int(data['qty'])

print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {price:.2f}")