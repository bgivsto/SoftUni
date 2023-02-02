def data_types(data, x):
    result = ""
    if data == "int":
        result = int(x) * 2
    elif data == "real":
        result = f"{float(x) * 1.5:.2f}"
    elif data == "string":
        result = f"${x}$"
    return result


data = input()
x = input()
print(data_types(data, x))
