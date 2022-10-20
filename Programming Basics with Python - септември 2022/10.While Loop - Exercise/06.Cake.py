width = int(input())
length = int(input())

pieces = width * length

while pieces > 0:
    entry = input()
    if entry == 'STOP':
        break
    pieces -= int(entry)
    if pieces < 0:
        print(f"No more cake left! You need {abs(pieces)} pieces more.")
        break

if pieces > 0:
    print(f"{pieces} pieces are left.")



