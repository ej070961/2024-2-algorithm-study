import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) 

dp = [0] * N

for i in range(N-1, -1, -1):
    dp[i] = 1
    for j in range(N-1, i, -1):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
