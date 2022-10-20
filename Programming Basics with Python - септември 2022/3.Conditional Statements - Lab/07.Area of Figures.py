from math import pi

figure_type = input()

if figure_type == 'square':
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure_type == 'circle':
    radius = float(input())
    area = pi * radius ** 2
    print(f"{area:.3f}")
elif figure_type == 'triangle':
    side_a = float(input())
    h = float(input())
    area = side_a * h / 2
    print(f"{area:.3f}")