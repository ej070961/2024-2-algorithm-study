# 1149 RGB거리
import sys

input = sys.stdin.readline

n = int(input())

rgb = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0] = rgb[0]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i][0] # R 계산
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i][1] # G 계산
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i][2] # B 계산 

print(min(dp[n-1])) # dp 에 저장 되어있는 것들 중최솟값