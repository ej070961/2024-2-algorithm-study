# n번째 계단까지 최고 점수 dp[n]
# dp[n] = max(dp[n-1], dp[n-2]), 단, dp[n-1]이 dp[n-2]를 거쳤다면, 선택 불가
import sys

input = sys.stdin.readline

N = int(input().strip())

stairs = []

for _ in range(N):
  stairs.append(int(input().strip()))

# 예외 처리 (계단 수가 1,2인 경우)
if N == 1: 
  print(stairs[0])
  sys.exit(0)

if N == 2:
  print(stairs[0] + stairs[1])
  sys.exit(0)

# dp[0][n]: n-2번째 계단 거침 => max(dp[0][n-2] or dp[1][n-2]) + stairs[n]
# dp[1][n]: n-1번째 계단 거침 => dp[0][n-1] + stairs[n]
dp = list([0] * N for _ in range(2))

dp[0][0] = stairs[0]
dp[0][1] = stairs[1]
dp[1][1] = stairs[0] + stairs[1]


for i in range(2, N): 
  dp[0][i] = max(dp[1][i - 2], dp[0][i - 2]) + stairs[i]
  dp[1][i] = dp[0][i - 1] + stairs[i]

print(max(dp[0][N - 1], dp[1][N - 1]))
