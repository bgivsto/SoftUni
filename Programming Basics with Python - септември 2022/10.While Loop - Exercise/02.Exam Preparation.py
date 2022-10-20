allowed_bad_grades = int(input())

bad_grades = 0
task_counter = 0
scores = 0
last_task = ''
failed = True

while bad_grades < allowed_bad_grades:
    task = input()
    if task == 'Enough':
        failed = False
        break
    else:
        last_task = task
        task_counter += 1
        grade = int(input())
        scores += grade
        if grade <= 4:
            bad_grades += 1

avg_grade = scores / task_counter

if not failed:
    print(f'Average score: {avg_grade:.2f}')
    print(f'Number of problems: {task_counter}')
    print(f'Last problem: {last_task}')
else:
    print(f'You need a break, {bad_grades} poor grades.')

