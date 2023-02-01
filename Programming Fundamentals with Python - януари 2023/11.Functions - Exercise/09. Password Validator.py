def is_valid(password):
    letters = 0
    digits = 0
    other = 0
    valid = True
    for i in password:
        if i.isalpha():
            letters += 1
        elif i.isnumeric():
            digits += 1
        else:
            other += 1
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    if other:
        print("Password must consist only of letters and digits")
        valid = False
    if not digits >= 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid:
        print("Password is valid")



password = input()

is_valid(password)