lst = [int(x) for x in input().split(" ")]

while True:
    manipulation = input()

    if manipulation == "end":
        print(lst)
        break

    elif "exchange" in manipulation:
        index = int(manipulation.split(" ")[1])
        if index not in range(len(lst)):
            print("Invalid index")
        else:
            lst = lst[index + 1:] + lst[:index + 1]

    elif "max" in manipulation or "min" in manipulation:
        even_list = [x for x in lst if x % 2 == 0]
        odd_list = [x for x in lst if x % 2 == 1]
        command = manipulation.split(" ")[0]
        number_type = manipulation.split(" ")[1]

        if command == "max":
            if number_type == "even":
                if even_list:
                    print(max(index for index, value in enumerate(lst) if value == max(even_list)))
                else:
                    print("No matches")
            elif number_type == "odd":
                if odd_list:
                    print(max(index for index, value in enumerate(lst) if value == max(odd_list)))
                else:
                    print("No matches")
        elif command == "min":
            if number_type == "even":
                if even_list:
                    print(max(index for index, value in enumerate(lst) if value == min(even_list)))
                else:
                    print("No matches")
            elif number_type == "odd":
                if odd_list:
                    print(max(index for index, value in enumerate(lst) if value == min(odd_list)))
                else:
                    print("No matches")

    elif "first" in manipulation or "last" in manipulation:
        command = manipulation.split(" ")[0]
        count = int(manipulation.split(" ")[1])
        number_type = manipulation.split(" ")[2]
        if count > len(lst):
            print("Invalid count")
        else:
            first_even = [x for x in lst if x % 2 == 0][:count]
            first_odd = [x for x in lst if x % 2 == 1][:count]
            last_even = [x for x in lst[::-1] if x % 2 == 0][:count]
            last_odd = [x for x in lst[::-1] if x % 2 == 1][:count]

            if command == "first":
                if number_type == "even":
                    print(first_even)
                elif number_type == "odd":
                    print(first_odd)
            elif command == "last":
                if number_type == "even":
                    print(last_even[::-1])
                elif number_type == "odd":
                    print(last_odd[::-1])
