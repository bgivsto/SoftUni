trip_price = float(input())
puzzles_qty = int(input())
talking_dolls_qty = int(input())
teddy_bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

toys_qty = puzzles_qty + talking_dolls_qty + teddy_bears_qty + minions_qty + trucks_qty

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = puzzle_price * puzzles_qty + talking_doll_price * talking_dolls_qty + teddy_bear_price * teddy_bears_qty + minion_price * minions_qty + truck_price * trucks_qty

if toys_qty >= 50:
    total_price = total_price * 0.75

rent = total_price * 0.1

earned_money = total_price - rent

if earned_money >= trip_price:
    print(f'Yes! {earned_money-trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - earned_money:.2f} lv needed.')

