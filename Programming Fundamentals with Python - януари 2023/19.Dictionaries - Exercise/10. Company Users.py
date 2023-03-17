database = {}

while True:
    line = input()

    if line == "End":
        break

    company, employee = line.split(" -> ")

    if company not in database:
        database[company] = [employee]
    else:
        if employee not in database[company]:
            database[company].append(employee)

for company in database.keys():
    print(company)
    for employee in database[company]:
        print(f"-- {employee}")