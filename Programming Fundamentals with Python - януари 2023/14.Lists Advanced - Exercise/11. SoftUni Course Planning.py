lessons = input().split(", ")

while True:
    entry = input()
    if entry == "course start":
        break

    elif "Add" in entry:
        title = entry.split(":")[1]
        if title not in lessons:
            lessons.append(title)

    elif "Insert" in entry:
        title, index = entry.split(":")[1], int(entry.split(":")[2])
        if title not in lessons:
            lessons.insert(index, title)

    elif "Exercise" in entry:
        title = entry.split(":")[1]
        if title in lessons:
            index = lessons.index(title)
            if title + "-Exercise" not in lessons:
                if index == len(lessons) - 1:
                    lessons.append(title + "-Exercise")
                else:
                    lessons.insert(index + 1, title + "-Exercise")
        elif title not in lessons:
            lessons.append(title)
            lessons.append(title + "-Exercise")

    elif "Remove" in entry:
        title = entry.split(":")[1]
        if title in lessons:
            lessons.remove(title)
            if title + "-Exercise" in lessons:
                lessons.remove(title + "-Exercise")

    elif "Swap" in entry:
        title1, title2 = entry.split(":")[1], entry.split(":")[2]
        if title1 and title2 in lessons:
            title1_index = lessons.index(title1)
            title2_index = lessons.index(title2)
            lessons[title1_index], lessons[title2_index] = lessons[title2_index], lessons[title1_index]
            if title1 + "-Exercise" in lessons:
                lessons.insert(title2_index+1, lessons.pop(lessons.index(title1 + "-Exercise")))
            if title2 + "-Exercise" in lessons:
                lessons.insert(title1_index+1, lessons.pop(lessons.index(title2 + "-Exercise")))

for index, lesson in enumerate(lessons, start=1):
    print(f"{index}.{lesson}")