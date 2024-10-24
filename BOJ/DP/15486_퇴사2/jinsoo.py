import sys

input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)



profit = 0

for i in range(n):
    profit = max(profit, dp[i])
    if i + meeting[i][0] >= n+1:
        continue
    dp[i + meeting[i][0]] = max(profit + meeting[i][1], dp[i + meeting[i][0]])
print(max(dp))

# 시간 복잡도 O(n)