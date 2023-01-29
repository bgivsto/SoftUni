def calculate(water, value, total_effort, cells):
    water -= int(value)
    effort = value * 0.25
    total_effort += effort
    cells.append(int(value))
    return water, total_effort, cells


high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)
fires = input().split("#")
water = int(input())
effort = 0
total_effort = 0
cells = []

for fire in fires:
    if water == 0:
        break

    fire_type, value = fire.split(" = ")[0], int(fire.split(" = ")[1])

    if fire_type == "High":
        if value in high and value <= water:
            water, total_effort, cells = calculate(water, value, total_effort, cells)

    elif fire_type == "Medium":
        if value in medium and value <= water:
            water, total_effort, cells = calculate(water, value, total_effort, cells)

    elif fire_type == "Low":
        if value in low and value <= water:
            water, total_effort, cells = calculate(water, value, total_effort, cells)


print("Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(cells)}")

