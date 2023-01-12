while True:
    new_string = ""
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for letter in string:
        new_string += 2 * letter
    print(new_string)
