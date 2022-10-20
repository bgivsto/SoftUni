n1 = int(input())
n2 = int(input())

for number in range(n1, n2+1):
    even_sum = 0
    odd_sum = 0

    for i, n in enumerate(str(number), start=1):
        if i % 2 == 1:
            odd_sum += int(n)
        else:
            even_sum += int(n)

    if odd_sum == even_sum:
        print(number, end=" ")
