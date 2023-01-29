# lst = [int(x) for x in input().split(", ")]
# beggars = int(input())
#
# shares = [[] for i in range(beggars)]
#
# while lst:
#     for i in range(beggars):
#         share = lst[0]
#         shares[i].append(share)
#         lst.remove(share)
#         if not lst:
#             break
#
# result = []
# for share in shares:
#     result.append(sum(share))
#
# print(result)

lst = [int(x) for x in input().split(", ")]
beggars = int(input())

result = []

for i in range(beggars):
    result.append(sum([lst[x] for x in range(i, len(lst), beggars)]))

print(result)
