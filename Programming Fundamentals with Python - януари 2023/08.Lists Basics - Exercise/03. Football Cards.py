team_a = [x for x in range(1, 12)]
team_b = [x for x in range(1, 12)]
cards = input().split(" ")
terminated = False

if cards:
    for element in cards:
        team, number = element.split("-")

        if team == "A":
            if int(number) in team_a:
                team_a.remove(int(number))
                if len(team_a) < 7:
                    terminated = True
                    break

        elif team == "B":
            if int(number) in team_b:
                team_b.remove(int(number))
                if len(team_b) < 7:
                    terminated = True
                    break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if terminated:
    print("Game was terminated")
