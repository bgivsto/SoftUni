number = input()

print("".join(str(n) for n in sorted([int(n) for n in number], reverse=True)))
