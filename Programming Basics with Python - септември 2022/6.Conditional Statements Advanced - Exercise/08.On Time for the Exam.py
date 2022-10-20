exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = hour_of_arrival * 60 + minute_of_arrival
time_difference = exam_time_in_minutes - arrival_time_in_minutes

if time_difference == 0:
    print('On time')
elif 0 < time_difference <= 30:
    print('On time')
    print(f"{time_difference} minutes before the start")
elif time_difference > 30:
    print('Early')
    if time_difference <= 59:
        print(f"{time_difference} minutes before the start")
    elif time_difference >= 60:
        hours = time_difference // 60
        minutes = time_difference % 60
        if minutes >= 10:
            print(f"{hours}:{minutes} hours before the start")
        else:
            print(f"{hours}:0{minutes} hours before the start")
elif time_difference < 0:
    print('Late')
    if abs(time_difference) <= 59:
        print(f"{abs(time_difference)} minutes after the start")
    elif abs(time_difference) >= 60:
        hours = abs(time_difference) // 60
        minutes = abs(time_difference) % 60
        if minutes >= 10:
            print(f"{hours}:{minutes} hours after the start")
        else:
            print(f"{hours}:0{minutes} hours after the start")



