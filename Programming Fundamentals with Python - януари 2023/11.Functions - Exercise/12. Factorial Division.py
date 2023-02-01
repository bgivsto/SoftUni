def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


def divide_factorial(a, b):
    return f"{factorial(a) / factorial(b):.2f}"


a = int(input())
b = int(input())

print(divide_factorial(a, b))
