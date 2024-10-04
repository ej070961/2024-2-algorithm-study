import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1) # i번째 음료까지 최대로 마실 수 있는 음료의 양
arr = [0] * (n+1)

for i in range(1,n+1,1):
    arr[i] = int(input())

dp[1] = arr[1]

if n >= 2:
    dp[2] = arr[1] + arr[2]  

# 3번째 음료부터 규칙 적용
for i in range(3, n + 1):
    # 세 가지 경우의 수:
    # 1. i-3번째 음료까지 먹고, i-1번째와 i번째 음료를 연속으로 먹은 경우
    # 2. i-2번째 음료 먹고, i-1번째 음료 건너뛰고, i번째 음료를 먹은 경우
    # 3. 현재 음료를 마시지 않는 경우 
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i-1])

print(max(dp))
