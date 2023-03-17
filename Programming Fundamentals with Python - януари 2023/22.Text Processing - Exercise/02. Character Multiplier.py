strings = input().split()
shorter = min(strings, key=len)
longer = max(strings, key=len)
if len(shorter) == len(longer):
    shorter, longer = strings[0], strings[1]
diff = len(longer) - len(shorter)
total_sum = 0

for i in range(len(shorter)):
    total_sum += ord(shorter[i]) * ord(longer[i])

for letter in longer[len(shorter):]:
    total_sum += ord(letter)

print(total_sum)