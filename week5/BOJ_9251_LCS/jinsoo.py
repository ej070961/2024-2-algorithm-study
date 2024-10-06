import sys

input = sys.stdin.readline

first = list(map(str,input().strip()))
second = list(map(str,input().strip()))

n = len(first)
m = len(second)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) # first[i-1] 과 second[j] , first[i] 와 second[j-1] 비교 (둘다 일치하지 않으면 긴 값을 찾아야 함)

print(dp[n][m])

# 풀이 참조