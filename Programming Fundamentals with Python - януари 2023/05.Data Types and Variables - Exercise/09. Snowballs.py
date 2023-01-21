import sys

snowballs = int(input())
temp_weight = -sys.maxsize
temp_time = -sys.maxsize
temp_quality = -sys.maxsize
temp_value = -sys.maxsize


for snowball in range(1, snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality
    if value > temp_value:
        temp_value = value
        temp_weight = weight
        temp_time = time
        temp_quality = quality

print(f"{temp_weight} : {temp_time} = {temp_value} ({temp_quality})")
