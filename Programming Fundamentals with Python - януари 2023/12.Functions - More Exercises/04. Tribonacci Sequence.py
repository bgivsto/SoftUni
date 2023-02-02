def tribonacci(n, memo={}):
    if n in {1, 2}:
        return 1
    if n == 3:
        return 2
    if n not in memo:
        memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    return memo[n]


n = int(input())
for i in range(1, n+1):
    print(tribonacci(i), end=" ")
