floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        if floor % 2 != 0 and floor != floors:
            print(f'A{floor}{room}', end=' ')
        elif floor % 2 == 0 and floor != floors:
            print(f'O{floor}{room}', end=' ')
        elif floor == floors:
            print(f'L{floor}{room}', end=' ')
    print()
