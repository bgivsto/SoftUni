def ascii(x, y):
    return " ".join([chr(i) for i in range(ord(x)+1, ord(y))])


x = input()
y = input()

print(ascii(x, y))