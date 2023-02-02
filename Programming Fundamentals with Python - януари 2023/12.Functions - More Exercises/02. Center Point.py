from math import floor
def closest_to_zero(x1, y1, x2, y2):
    distance1 = abs((x1**2 + y1**2)**0.5)
    distance2 = abs((x2**2 + y2**2)**0.5)
    if distance1 <= distance2:
        result = floor(x1), floor(y1)
    else:
        result = floor(x2), floor(y2)
    return result


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(closest_to_zero(x1, y1, x2, y2))

