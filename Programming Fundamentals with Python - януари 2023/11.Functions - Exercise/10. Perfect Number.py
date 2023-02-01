def is_perfect(n):
    if n == sum([x for x in range(1, n) if n % x == 0]):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())
is_perfect(n)