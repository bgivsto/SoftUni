decorations_to_buy = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spirit = 0
cost = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        decorations_to_buy += 2
    if day % 2 == 0:
        cost += ornament_set_price * decorations_to_buy
        spirit += 5
    if day % 3 == 0:
        cost += (tree_skirt_price + tree_garland_price) * decorations_to_buy
        spirit += 13
    if day % 5 == 0:
        cost += tree_lights_price * decorations_to_buy
        spirit += 17
    if day % 10 == 0:
        spirit -= 20
        cost += tree_skirt_price + tree_garland_price + tree_lights_price
        if day == days_until_christmas:
            spirit -= 30
    if day % 15 == 0:
        spirit += 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
