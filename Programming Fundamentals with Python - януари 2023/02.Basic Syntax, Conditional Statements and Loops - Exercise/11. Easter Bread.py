budget = float(input())
flour_price_1kg = float(input())
eggs_price_1kg = flour_price_1kg * 0.75
milk_price_1l = 1.25 * flour_price_1kg
milk_price_250ml = milk_price_1l / 4
loaf_price = eggs_price_1kg + flour_price_1kg + milk_price_250ml
loaves = 0
colored_eggs = 0

while budget >= loaf_price:
    budget -= loaf_price
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        lost_eggs = loaves - 2
        colored_eggs -= lost_eggs

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

