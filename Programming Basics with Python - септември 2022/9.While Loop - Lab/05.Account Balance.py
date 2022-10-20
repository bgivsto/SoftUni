entry = input()
money = 0

while entry != 'NoMoreMoney':
    if float(entry) < 0:
        print(f'Invalid operation!')
        break
    else:
        money += float(entry)
        print(f'Increase: {float(entry):.2f}')
    entry = input()

print(f'Total: {money:.2f}')
