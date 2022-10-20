days = int(input())
place = input()
rating = input()
nights = days - 1
price = ''

room_price = 18.00 * nights
apartment_price = 25.00 * nights
president_apartment_price = 35.00 * nights

if place == 'room for one person':
    if rating == 'positive':
        room_price *= 1.25
    elif rating == 'negative':
        room_price *= 0.9
    print(f"{room_price:.2f}")

if days < 10:
    if place == 'apartment':
        apartment_price *= 0.7
        if rating == 'positive':
            apartment_price *= 1.25
        elif rating == 'negative':
            apartment_price *= 0.9
        print(f"{apartment_price:.2f}")

    elif place == 'president apartment':
        president_apartment_price *= 0.9
        if rating == 'positive':
            president_apartment_price *= 1.25
        elif rating == 'negative':
            president_apartment_price *= 0.9
        print(f"{president_apartment_price:.2f}")

elif 10 <= days <= 15:
    if place == 'apartment':
        apartment_price *= 0.65
        if rating == 'positive':
            apartment_price *= 1.25
        elif rating == 'negative':
            apartment_price *= 0.9
        print(f"{apartment_price:.2f}")

    elif place == 'president apartment':
        president_apartment_price *= 0.85
        if rating == 'positive':
            president_apartment_price *= 1.25
        elif rating == 'negative':
            president_apartment_price *= 0.9
        print(f"{president_apartment_price:.2f}")

elif days > 15:
    if place == 'apartment':
        apartment_price *= 0.5
        if rating == 'positive':
            apartment_price *= 1.25
        elif rating == 'negative':
            apartment_price *= 0.9
        print(f"{apartment_price:.2f}")

    elif place == 'president apartment':
        president_apartment_price *= 0.8
        if rating == 'positive':
            president_apartment_price *= 1.25
        elif rating == 'negative':
            president_apartment_price *= 0.9
        print(f"{president_apartment_price:.2f}")


