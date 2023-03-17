import string

usernames = input().split(", ")
allowed = string.ascii_letters + string.digits + "_" + "-"

valid_username = []
for username in usernames:
    valid = True
    for letter in username:
        if letter not in allowed:
            valid = False
            break
    if valid:
        if len(username) in range(3, 17):
            valid_username.append(username)

print("\n".join(valid_username))
