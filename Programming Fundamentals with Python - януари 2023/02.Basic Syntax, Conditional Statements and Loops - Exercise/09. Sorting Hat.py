success = True

while True:
    command = input()
    if command == "Welcome!":
        break
    if command == "Voldemort":
        success = False
        print("You must not speak of that name!")
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

if success:
    print("Welcome to Hogwarts.")
