def calculate(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


operator = input()
a = int(input())
b = int(input())

print(calculate(a, b, operator))
