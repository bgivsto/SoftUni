electrons = int(input())
shell = 1
result = []

while electrons > 0:
    filled_shell = 2 * shell**2
    if electrons >= filled_shell:
        result.append(filled_shell)
    else:
        result.append(electrons)
    electrons -= filled_shell
    shell += 1

print(result)