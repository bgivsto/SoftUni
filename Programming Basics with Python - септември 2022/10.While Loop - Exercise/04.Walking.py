goal = 10000
total_steps = 0
go_home = False

while total_steps < goal and not go_home:
    entry = input()
    if entry == 'Going home':
        total_steps += int(input())
        go_home = True
        break
    else:
        total_steps += int(entry)

diff = abs(total_steps - goal)
if total_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")