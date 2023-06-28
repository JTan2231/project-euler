n = 20
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]

dp[0][0] = 1
for i in range(n + 1):
    for j in range(n + 1):
        if i:
            dp[i][j] += dp[i - 1][j]
        
        if j:
            dp[i][j] += dp[i][j - 1]

print(dp[-1][-1])