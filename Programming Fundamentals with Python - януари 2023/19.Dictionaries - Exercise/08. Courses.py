database = {}

while True:
    line = input()

    if line == "end":
        break

    course, name = line.split(" : ")
    if course not in database:
        database[course] = [name]
    else:
        database[course].append(name)

for course in database.keys():
    print(f"{course}: {len(database[course])}")
    for name in database[course]:
        print(f"-- {name}")



