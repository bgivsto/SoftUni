actor_name = input()
academy_points = float(input())
judges = int(input())
target_points = 1250.5

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    given_points = len(judge_name) * judge_points / 2
    academy_points += given_points
    if academy_points >= target_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points < target_points:
    print(f"Sorry, {actor_name} you need {target_points-academy_points:.1f} more!")