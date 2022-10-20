width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while free_space > 0:
    entry = input()
    if entry == 'Done':
        print(f"{free_space} Cubic meters left.")
        break
    free_space -= int(entry)
    if free_space < 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")

