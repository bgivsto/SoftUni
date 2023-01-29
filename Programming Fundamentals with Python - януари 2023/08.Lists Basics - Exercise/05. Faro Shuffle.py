deck = input().split(" ")
shuffles = int(input())

for i in range(shuffles):
    first_half = deck[:len(deck)//2]
    second_half = deck[len(deck)//2:]
    deck = []
    for tup in list(zip(first_half, second_half)):
        for item in tup:
            deck.append(item)

print(deck)

