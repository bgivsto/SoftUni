first_string = input()
second_string = input()
new_string = ""

for i in range(len(first_string)):
    new_string = second_string[:i+1] + first_string[i+1:]
    if first_string[i] != second_string[i]:
        print(new_string)
