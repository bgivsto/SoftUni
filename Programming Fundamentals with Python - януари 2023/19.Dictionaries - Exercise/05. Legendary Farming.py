items = {}
junk = {}

mapper = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

game_over = False
while not game_over:
    line = input().split()
    for i in range(0, len(line), 2):
        material = (line[i+1]).lower()
        qty = int(line[i])
        if material in mapper:
            if material in items:
                items[material] += qty
            else:
                items[material] = qty
            if items[material] >= 250:
                items[material] -= 250
                print(f"{mapper[material]} obtained!")
                game_over = True
                break
        else:
            if material in junk:
                junk[material] += qty
            else:
                junk[material] = qty

print(f"shards: {items.get('shards', 0)}")
print(f"fragments: {items.get('fragments', 0)}")
print(f"motes: {items.get('motes', 0)}")
for k, v in junk.items():
    print(f"{k}: {v}")