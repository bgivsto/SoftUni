initial_energy = 100
current_energy = initial_energy
coins = 100
events = input().split("|")

for event in events:
    command, number = event.split("-")[0], int(event.split("-")[1])

    if command == "rest":
        if current_energy + number > 100:
            print(f"You gained {initial_energy - current_energy} energy.")
            current_energy = 100
        else:
            current_energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {current_energy}.")

    elif command == "order":
        if current_energy >= 30:
            current_energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            if current_energy > 50:
                current_energy = 100
            else:
                current_energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
