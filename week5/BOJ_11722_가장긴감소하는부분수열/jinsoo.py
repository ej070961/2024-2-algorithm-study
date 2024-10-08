import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

dp = [0] * n


for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)+ 1)

# 간략하게 정리 현 위치가 이전보다 작다면 + 1 을 해주는 방식
# O(n^2)