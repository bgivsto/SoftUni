l = int(input())
w = int(input())
h = int(input())
percent = float(input())

volume = l * w * h
volume_liters = volume / 1000
needed_liters = volume_liters * (1-percent/100)

print(needed_liters)


