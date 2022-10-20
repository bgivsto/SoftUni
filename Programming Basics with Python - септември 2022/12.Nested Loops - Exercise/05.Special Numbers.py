n = int(input())

for number in range(1111, 10000):
    count = 0
    for digit in str(number):
        count += 1
        if int(digit) == 0 or n % int(digit) != 0:
            break
        if count == len(str(number)):
            print(number, end=" ")
