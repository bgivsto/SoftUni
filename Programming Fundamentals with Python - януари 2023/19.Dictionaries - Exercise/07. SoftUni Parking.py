n = int(input())

database = {}
for _ in range(n):
    line = input()

    if "unregister" not in line:
        name, number = line.split()[1], line.split()[2]
        if name not in database:
            database[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif "unregister" in line:
        name = line.split()[1]
        if name not in database:
            print(f"ERROR: user {name} not found")
        else:
            database.pop(name)
            print(f"{name} unregistered successfully")

for name, number in database.items():
    print(f"{name} => {number}")