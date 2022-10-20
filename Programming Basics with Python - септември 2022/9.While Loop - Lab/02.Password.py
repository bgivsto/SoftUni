name = input()
password = input()
password_guess = input()

while password_guess != password:
    password_guess = input()

print(f'Welcome {name}!')
