def odd_and_even(n):
    odd = sum([int(x) for x in n if int(x) % 2 == 1])
    even = sum([int(x) for x in n if int(x) % 2 == 0])
    print(f"Odd sum = {odd}, Even sum = {even}")


n = input()
odd_and_even(n)
