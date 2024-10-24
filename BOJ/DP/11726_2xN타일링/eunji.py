import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
#n이 1이면 2*1 방법 하나
dp[1] = 1

if n == 1: 
    print(1)
elif n ==2: 
    print(2)

else: 
    #n이 2이면 1*2 2개, 2*1 2개 사용하는 방법 2개
    dp[2] = 2
    #n이 3부터는 i-2 번째 방법에 = 붙인거, i-1번째 방법에 ㅣ 붙이는 방법이 있음
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    print(dp[n]%10007)