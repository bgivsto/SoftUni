deposit = float(input())
period = int(input())
percent = float(input())

total_sum = deposit + period * ((deposit * percent / 100) / 12)

print(total_sum)
