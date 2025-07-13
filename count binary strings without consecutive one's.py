MOD = 10**9 + 7

def count_valid_binary_strings(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    a, b = 1, 2  # dp[0] = 1, dp[1] = 2
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b

# Input: single line, integer
n = int(input())
print(count_valid_binary_strings(n))
