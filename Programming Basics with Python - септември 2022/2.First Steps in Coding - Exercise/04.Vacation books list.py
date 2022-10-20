pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_read_time = pages // pages_per_hour
needed_hours = total_read_time / days

print(int(needed_hours))
