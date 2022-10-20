pen_packets = int(input())
marker_packets = int(input())
cleaner = int(input())
discount = int(input())

pen_price = 5.80
marker_price = 7.20
cleaner_price = 1.20

current_discount = (1-discount/100)
current_pen_price = pen_packets * pen_price * current_discount
current_marker_price = marker_packets * marker_price * current_discount
current_cleaner_price = cleaner_price * cleaner * current_discount

total_price = current_marker_price + current_cleaner_price + current_pen_price

print(f"{total_price:.2f}")

