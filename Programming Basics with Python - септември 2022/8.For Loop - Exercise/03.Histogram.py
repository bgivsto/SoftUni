n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    else:
        p5 += 1

p1_result = (p1 / n) * 100
p2_result = (p2 / n) * 100
p3_result = (p3 / n) * 100
p4_result = (p4 / n) * 100
p5_result = (p5 / n) * 100

print(f"{p1_result:.2f}%")
print(f"{p2_result:.2f}%")
print(f"{p3_result:.2f}%")
print(f"{p4_result:.2f}%")
print(f"{p5_result:.2f}%")