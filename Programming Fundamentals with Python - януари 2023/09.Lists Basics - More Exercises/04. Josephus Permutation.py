# def find_index(k, lst):
#     index = (k % len(lst)) - 1
#     if index >= len(lst):
#         k = index
#         return find_index(k, lst)
#     return index
#
#
# people = [int(x) for x in input().split()]
# k = int(input())
#
# result = []
# while people:
#     index = find_index(k, people)
#     result.append(people.pop(index))
#     if index == -1:
#         index = 0
#     people = people[index:] + people[:index]
#
# print(f'[{",".join([str(x) for x in result])}]')

input_list = list(input().split())
n = int(input())

killed = []
index = 0

while input_list:
    index = (index + n - 1) % len(input_list)
    killed.append(input_list.pop(index))

print("[" + ",".join(killed) + "]")