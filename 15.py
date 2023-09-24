n = 21

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1
for i in range(0, n):
    for j in range(0, n):
        if i != 0:
            dp[i][j] += dp[i-1][j]
        if j != 0:
            dp[i][j] += dp[i][j-1]

print(dp[20][20])
