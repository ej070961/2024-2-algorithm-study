import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007 
    # 10007 로 나눈 나머지 값을 출력하는 이유 -> dp 는 결과가 매우 커질 수 있기 때문에 10007 미만의 수를 출력하기 위함

print(dp[n])