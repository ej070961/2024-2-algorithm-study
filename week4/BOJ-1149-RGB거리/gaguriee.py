import sys
input = sys.stdin.readline

n = int(input()) 
cost = [list(map(int, input().split())) for _ in range(n)]  # 각 집을 빨강, 초록, 파랑으로 칠하는 비용

dp = [[0] * 3 for _ in range(n)]

# 첫 번째 집 비용 초기화
dp[0][0] = cost[0][0]  # 빨강
dp[0][1] = cost[0][1]  # 초록
dp[0][2] = cost[0][2]  # 파랑

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # i번째 집을 빨강으로 칠할 때 최소 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # i번째 집을 초록으로 칠할 때 최소 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # i번째 집을 파랑으로 칠할 때 최소 비용

# 마지막 집을 각각 빨강, 초록, 파랑으로 칠하는 경우의 최소 비용 중 최솟값 출력
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
