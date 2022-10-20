name = input()
grade = 1
failed = 0
grades_sum = 0
annual_grade = 0

while failed < 2 and grade <= 12:
    annual_grade = float(input())
    if annual_grade < 4.00:
        failed += 1
        continue
    else:
        grade += 1
    grades_sum += annual_grade

if failed >= 2:
    print(f'{name} has been excluded at {grade} grade')
else:
    avg_grade = grades_sum / 12
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')

