city = input()
sales_volume = float(input())
flag = True
rate = 0

if city == 'Sofia':
    if 0 <= sales_volume <= 500:
        rate = 0.05
    elif 500 < sales_volume <= 1000:
        rate = 0.07
    elif 1000 < sales_volume <= 10000:
        rate = 0.08
    elif sales_volume > 10000:
        rate = 0.12
    else:
        flag = False

elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        rate = 0.045
    elif 500 < sales_volume <= 1000:
        rate = 0.075
    elif 1000 < sales_volume <= 10000:
        rate = 0.1
    elif sales_volume > 10000:
        rate = 0.13
    else:
        flag = False

elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        rate = 0.055
    elif 500 < sales_volume <= 1000:
        rate = 0.08
    elif 1000 < sales_volume <= 10000:
        rate = 0.12
    elif sales_volume > 10000:
        rate = 0.145
    else:
        flag = False

else:
    flag = False

if flag:
    print(f"{sales_volume * rate:.2f}")
else:
    print('error')
