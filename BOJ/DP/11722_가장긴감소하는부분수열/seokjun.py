import sys
readline = sys.stdin.readline

N = int(readline())
arr = list(map(int, readline().split(" ")))

"""
정의) 
dp[n]: n번째 수로 끝나는 목표 수열의 최대 길이.
관계식)
목표 수열의 k번째 원소는 k-1번째 원소보다 작음.
dp[i] = dp[j] + 1
j: 0부터 i-1번째 수 중에서 arr[j] > arr[i]인 것 중 dp가 가장 큰 것.
"""

dp = list([1] * N)

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))