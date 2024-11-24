from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10**9)

dp = [1, 1, 2, 6, 24, 120, 720] + [0] * 3000
for i in range(2, 2025):
    dp[i] = (i - 1) * dp[i - 1]
    
print((dp[2024] + 2 * dp[2023]) // dp[2022])

