import sys
input = sys.stdin.readline

N = int(input())
time = [0] * (N+1)
price = [0] * (N+1)
dp = [0] * (N+1)

for i in range(1, N+1):
    T, P = map(int, input().split())
    time[i] = T
    price[i] = P

max_profit = 0  # 지금까지 벌 수 있는 최대 금액

for i in range(1, N+1):
    # i일까지 벌 수 있는 최대 금액을 갱신
    max_profit = max(max_profit, dp[i-1])

    # i일에 상담을 할 수 있는 경우
    if i + time[i] - 1 <= N:
        dp[i + time[i] - 1] = max(dp[i + time[i] - 1], max_profit + price[i])

print(max(dp))
