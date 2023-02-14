notes = [0] * 10

while True:
    entry = input()
    if entry == "End":
        break

    importance, note = int(entry.split("-")[0]) - 1, entry.split("-")[1]
    notes.pop(importance)
    notes.insert(importance, note)

result = [el for el in notes if el != 0]
print(result)
