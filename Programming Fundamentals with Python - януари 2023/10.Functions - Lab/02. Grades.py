def grade(n):
    if 2 <= n <= 2.99:
        print("Fail")
    elif 3 <= n <= 3.49:
        print("Poor")
    elif 3.50 <= n <= 4.49:
        print("Good")
    elif 4.50 <= n <= 5.49:
        print("Very Good")
    elif 5.50 <= n <= 6:
        print("Excellent")

n = float(input())
grade(n)

