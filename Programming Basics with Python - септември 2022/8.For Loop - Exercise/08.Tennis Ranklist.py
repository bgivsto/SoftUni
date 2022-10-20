from math import floor

tournaments_count = int(input())
starting_points = int(input())
wins = 0

tournament_points = 0
for i in range(tournaments_count):
    stage = input()
    if stage == 'W':
        tournament_points += 2000
        wins += 1
    elif stage == 'F':
        tournament_points += 1200
    elif stage == 'SF':
        tournament_points += 720

total_points = starting_points + tournament_points
average_points = floor(tournament_points / tournaments_count)
win_rate = wins * 100 / tournaments_count

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_rate:.2f}%")