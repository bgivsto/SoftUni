herd = input().split(", ")

if herd[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_number = herd[::-1].index("wolf")
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
