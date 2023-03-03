courses = {}
while True:
    entry = input()
    if ":" not in entry:
        entry = entry.replace("_", " ")
        for k, v in courses[entry].items():
            print(f"{k} - {v}")
        break
    else:
        name, ID, course = entry.split(":")
        if course not in courses:
            courses[course] = {name: ID}
        else:
            courses[course][name] = ID
