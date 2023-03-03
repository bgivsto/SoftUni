contacts = {}

while True:
    entry = input()
    if entry.isnumeric():
        break

    name, number = entry.split("-")
    contacts[name] = number

for _ in range(int(entry)):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
