train = [0 for _ in range(int(input()))]

while True:
    command = input()
    if command == "End":
        break

    elif "add" in command:
        people = int(command.split()[1])
        train[-1] += people

    else:
        index = int(command.split()[1])
        people = int(command.split()[2])

        if "insert" in command:
            train[index] += people

        elif "leave" in command:
            train[index] -= people

print(train)
