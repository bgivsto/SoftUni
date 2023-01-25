n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

if command == "even":
    print([x for x in numbers if x % 2 == 0])
elif command == "odd":
    print([x for x in numbers if x % 2 == 1])
elif command == "negative":
    print([x for x in numbers if x < 0])
elif command == "positive":
    print([x for x in numbers if x >= 0])

