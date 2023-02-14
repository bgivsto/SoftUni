nums = [int(x) for x in input().split(", ")]
print([i for i, k in enumerate(nums) if k % 2 == 0])
