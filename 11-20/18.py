n = 15
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0, n):
    nums = input().split(" ")
    for j in range(0, len(nums)):
        dp[i][j] = int(nums[j])


res = 0
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
        res = max(res, dp[i][j])

print(res)
