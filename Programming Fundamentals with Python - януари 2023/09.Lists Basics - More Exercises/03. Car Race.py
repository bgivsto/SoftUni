times = [int(x) for x in input().split()]
middle = len(times) // 2
left_times = times[:middle]
right_times = times[middle+1:][::-1]
left = 0
right = 0

for i in range(len(left_times)):
    if left_times[i] == 0:
        left *= 0.8
    else:
        left += left_times[i]

for i in range(len(right_times)):
    if right_times[i] == 0:
        right *= 0.8
    else:
        right += right_times[i]

winner = ""
if left < right:
    winner = "left"
elif right < left:
    winner = "right"

print(f"The winner is {winner} with total time: {min(left, right):.1f}")