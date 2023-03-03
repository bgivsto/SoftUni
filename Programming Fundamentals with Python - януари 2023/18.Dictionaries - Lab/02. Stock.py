products = input().split()
search = input().split()
pairs = {}

for i in range(0, len(products), 2):
    pairs[products[i]] = int(products[i+1])

for item in search:
    if item in pairs:
        print(f"We have {pairs[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
