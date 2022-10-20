total_tickets = 0
total_standard_tickets = 0
total_student_tickets = 0
total_kid_tickets = 0

while True:
    movie = input()
    if movie == 'Finish':
        break

    current_total_tickets = 0
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    free_seats = int(input())
    total_free_seats = free_seats

    while free_seats:
        ticket = input()
        if ticket == 'End':
            break

        elif ticket == 'student':
            student_tickets += 1
            total_student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
            total_standard_tickets += 1
        elif ticket == 'kid':
            total_kid_tickets += 1
            kid_tickets += 1

        free_seats -= 1
        current_total_tickets = student_tickets + standard_tickets + kid_tickets

    total_tickets += current_total_tickets

    print(f"{movie} - {current_total_tickets*100/total_free_seats:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets*100/total_tickets:.2f}% student tickets.")
print(f"{total_standard_tickets*100/total_tickets:.2f}% standard tickets.")
print(f"{total_kid_tickets*100/total_tickets:.2f}% kids tickets.")