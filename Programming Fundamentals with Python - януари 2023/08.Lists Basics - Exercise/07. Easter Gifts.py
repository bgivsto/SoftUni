gifts = input().split()

while True:
    entry = input()

    if entry == "No Money":
        break

    if "OutOfStock" in entry:
        gift = entry.split()[1]
        for i, element in enumerate(gifts):
            if element == gift:
                gifts[i] = None

    elif "Required" in entry:
        gift, index = entry.split()[1], int(entry.split()[2])
        if index in range(len(gifts)):
            gifts[index] = gift

    elif "JustInCase" in entry:
        gift = entry.split()[1]
        gifts[-1] = gift

print(" ".join([gift for gift in gifts if gift is not None]))