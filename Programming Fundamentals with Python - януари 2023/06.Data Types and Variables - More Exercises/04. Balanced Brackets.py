n = int(input())
message = ""
lst = []

for i in range(n):
    entry = input()
    if entry == "(" or entry == ")":
        if "(" not in lst and entry == ")":
            print("UNBALANCED")
            break
        elif entry == "(" and "(" in lst:
            print("UNBALANCED")
            break
        elif entry == ")" and "(" in lst:
            lst.pop(lst.index("("))
        else:
            lst.append(entry)
else:
    print("BALANCED")

