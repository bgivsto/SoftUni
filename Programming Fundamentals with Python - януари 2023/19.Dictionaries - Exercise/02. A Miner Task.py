result = {}

while True:
    entry = input()
    if entry == "stop":
        for k, v in result.items():
            print(f"{k} -> {v}")
        break
    else:
        resource = entry
        quantity = int(input())
        if resource not in result:
            result[resource] = quantity
        else:
            result[resource] += quantity
