import sys
input = sys.stdin.readline

N = int(input()) 

stair = [0] * (N + 1)
for i in range(1, N + 1):
    stair[i] = int(input())

# dp[i]는 i번째 계단까지의 최대 점수
dp = [0] * (N + 1)

# 첫 번째 계단은 반드시 밟아야 하므로, dp[1] = stair[1]
dp[1] = stair[1]

if N >= 2:
    dp[2] = stair[1] + stair[2]  # 두 번째 계단까지의 최대 점수

# 3번째 계단부터는 규칙을 적용
for i in range(3, N + 1):
    # 두 가지 경우의 수:
    # 1. i-1 계단에서 한 계단 올라온 경우 (i-1을 밟고, i-2는 밟지 않음)
    # 2. i-2 계단에서 두 계단 올라온 경우 (i-2에서 바로 올라옴)
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[N])
