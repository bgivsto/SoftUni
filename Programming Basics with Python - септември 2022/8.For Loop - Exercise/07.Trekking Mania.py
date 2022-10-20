groups = int(input())

musala_people = 0
monblan_people = 0
kilimandjaro_people = 0
k2_people = 0
everest_people = 0
total_people = 0

for i in range(groups):
    group_members = int(input())
    total_people += group_members
    if group_members <= 5:
        musala_people += group_members
    elif 6 <= group_members <= 12:
        monblan_people += group_members
    elif 13 <= group_members <= 25:
        kilimandjaro_people += group_members
    elif 26 <= group_members <= 40:
        k2_people += group_members
    elif group_members >= 41:
        everest_people += group_members

musala_people_result = musala_people * 100 / total_people
monblan_people_result = monblan_people * 100 / total_people
kilimandjaro_people_result = kilimandjaro_people * 100 / total_people
k2_people_result = k2_people * 100 / total_people
everest_people_result = everest_people * 100 / total_people

print(f"{musala_people_result:.2f}%")
print(f"{monblan_people_result:.2f}%")
print(f"{kilimandjaro_people_result:.2f}%")
print(f"{k2_people_result:.2f}%")
print(f"{everest_people_result:.2f}%")


