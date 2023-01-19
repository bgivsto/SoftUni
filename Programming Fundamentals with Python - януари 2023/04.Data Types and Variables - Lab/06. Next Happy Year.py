number = int(input()) + 1

while True:
    for char in str(number):
        count = str(number).count(char)
        if count > 1:
            break
    else:
        print(number)
        break
    number += 1
