text = input()

i = 0
while i < len(text):
    if text[i] == ":":
        print(f":{text[i+1]}")
    i += 1

