sequence = [int(x) for x in input().split()]
result = 0

while len(sequence) > 0:
    index = int(input())
    if index < 0:
        captured = sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif index >= len(sequence):
        captured = sequence.pop(-1)
        sequence.append(sequence[0])
    else:
        captured = sequence.pop(index)

    result += captured
    sequence = [x + captured if x <= captured else x - captured for x in sequence]

print(result)
