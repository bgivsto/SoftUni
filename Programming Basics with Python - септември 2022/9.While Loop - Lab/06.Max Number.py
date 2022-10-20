max_number = float('-inf')

while True:
    entry = input()
    if entry == 'Stop':
        break
    else:
        if max_number < int(entry):
            max_number = int(entry)

print(int(max_number))
