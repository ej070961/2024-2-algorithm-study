import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 3 # 1 + 1 + 1

if N >= 2:
    dp[2] = 7 # 2 + 2 + 3

    for i in range(3, N + 1):
        dp[i] = ( dp[i-2] + 2 * dp[i-1] ) % 9901

print(dp[N])