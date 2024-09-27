N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]

dp[1][0] = 1
dp[1][1] = 2 

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 9901
    dp[i][1] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % 9901

result = (dp[N][0] + dp[N][1]) % 9901
print(result)
