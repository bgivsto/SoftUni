text = input()

digits = []
non_digits = []
for char in text:
    if char.isdigit():
        digits.append(int(char))
    else:
        non_digits.append(char)

take_list = []
skip_list = []
for index, digit in enumerate(digits):
    if index % 2 == 0:
        take_list.append(digit)
    else:
        skip_list.append(digit)

zipped = list(zip(take_list, skip_list))
take_and_skip = []
for tup in zipped:
    for el in tup:
        take_and_skip.append(el)

result = ""
for i in range(len(take_and_skip) - 1):
    if i % 2 == 0:
        result += "".join(non_digits[:take_and_skip[i]])
        del non_digits[:take_and_skip[i]]
    else:
        non_digits = non_digits[take_and_skip[i]:]

print(result)