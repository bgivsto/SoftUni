def is_palindrome(n):
    if n == n[::-1]:
        return True
    return False


n = [is_palindrome(x) for x in input().split(", ")]
print("\n".join(str(x) for x in n))