rooms = int(input())
enough = True
total_free_chairs = 0

for room in range(1, rooms + 1):
    info = input().split()
    chairs, visitors = int(info[0].count("X")), int(info[1])

    total_free_chairs += chairs - visitors

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        enough = False

if enough:
    print(f"Game On, {total_free_chairs} free chairs left")