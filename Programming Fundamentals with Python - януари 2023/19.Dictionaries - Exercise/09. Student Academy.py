n = int(input())

students = {}
for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for student in students.keys():
    avg_grade = sum(students[student]) / len(students[student])
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")
