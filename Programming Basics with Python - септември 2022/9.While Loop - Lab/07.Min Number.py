min_number = float('inf')

while True:
    entry = input()
    if entry == 'Stop':
        break
    else:
        if min_number > int(entry):
            min_number = int(entry)

print(int(min_number))

