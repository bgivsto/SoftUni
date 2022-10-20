prime_sum = 0
non_prime_sum = 0


while True:
    entry = input()
    if entry == 'stop':
        break
    if int(entry) < 0:
        print('Number is negative.')
        continue
    prime = True
    for i in range(2, int(entry)):
        if int(entry) % i == 0:
            prime = False
            break
    if prime:
        prime_sum += int(entry)
    else:
        non_prime_sum += int(entry)


print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
