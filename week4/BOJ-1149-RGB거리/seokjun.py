import sys
input = sys.stdin.readline

N = int(input().strip())
cost = []

for _ in range(N):
  cost.append(list(map(int, input().split(" "))))

dp = [[0] * 3 for _ in range(N)]

for i in range(3):
  dp[0][i] = cost[0][i]

for i in range(1, N):
  dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))