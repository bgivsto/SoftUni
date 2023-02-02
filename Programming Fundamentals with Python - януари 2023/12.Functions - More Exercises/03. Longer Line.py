from math import floor, acos, sqrt, cos
def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    distance1 = abs((x1**2 + y1**2)**0.5)
    distance2 = abs((x2**2 + y2**2)**0.5)
    distance3 = abs((x3**2 + y3**2)**0.5)
    distance4 = abs((x4**2 + y4**2)**0.5)
    angle1 = acos(y1 / distance1) + acos(y2 / distance2)
    angle2 = acos(y3 / distance3) + acos(y4 / distance4)
    line1 = sqrt(distance1**2 + distance2**2 - 2 * distance1 * distance2 * cos(angle1))
    line2 = sqrt(distance3**2 + distance4**2 - 2 * distance3 * distance4 * cos(angle2))
    if line1 >= line2:
        if distance1 <= distance2:
            result = f"({x1}, {y1})({x2}, {y2})"
        else:
            result = f"({x2}, {y2})({x1}, {y1})"
    else:
        if distance3 <= distance4:
            result = f"({x3}, {y3})({x4}, {y4})"
        else:
            result = f"({x4}, {y4})({x3}, {y3})"
    return result


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
x3 = floor(float(input()))
y3 = floor(float(input()))
x4 = floor(float(input()))
y4 = floor(float(input()))

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
