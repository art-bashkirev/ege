dp = [0] * 2030
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(2, 2030):
    dp[i] = dp[i - 1] * (i - 1)

print((dp[2024] + 2 * dp[2023]) / dp[2022])