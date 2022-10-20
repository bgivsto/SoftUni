fav_book = input()
book_counter = 0

while True:
    book = input()
    if book == fav_book or book == 'No More Books':
        break
    else:
        book_counter += 1

if book == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')
else:
    print(f'You checked {book_counter} books and found it.')

