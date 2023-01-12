budget = int(input())

while not budget < 0:
    entry = input()
    if entry == "End":
        break
    budget -= int(entry)

if budget < 0:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
