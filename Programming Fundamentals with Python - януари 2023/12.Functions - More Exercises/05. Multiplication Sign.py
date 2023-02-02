def multiplication_sign(a, b, c):
    lst = [a, b, c]
    negatives = 0

    for num in lst:
        if num == 0:
            return "zero"
        elif num < 0:
            negatives += 1

    if negatives % 2 == 1:
        return "negative"

    return "positive"


a = int(input())
b = int(input())
c = int(input())

print(multiplication_sign(a, b, c))
