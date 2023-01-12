coffees = 0

while True:
    entry = input()
    if entry == "END":
        break
    if entry.lower() in ["dog", "cat", "movie", "coding"]:
        if entry.islower():
            coffees += 1
        elif entry.isupper():
            coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
