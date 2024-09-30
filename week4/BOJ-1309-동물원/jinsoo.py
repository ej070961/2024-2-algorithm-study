# BOJ-1309-동물원

import sys

input = sys.stdin.readline

n = int(input())

# 점화식 아무리 해도 찾기 너무 힘듦
# n = 4 까지 해봄
dp = [[0]*3 for _ in range(n+1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
for i in range(2,n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) %9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) %9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) %9901
# print(f"n: {n}")
# print("dp table: ")
# for i in range(1, n+1):
#     print(dp[i])
# [1, 1, 1]
# [3, 2, 2]
# [7, 5, 5]
# [17, 12, 12]

print((dp[n][0]+dp[n][1]+dp[n][2])%9901)