import sys

input = sys.stdin.readline

n = int(input())

wine = []
for _ in range(n):
    wine.append(int(input()))

if n == 1:
    print(wine[0])
    sys.exit() # 이걸 설정 안해줬더니 runtime error 가 떴다. n 이 1 또는 2일 수도 있었구나 ...
elif n == 2:
    print(wine[0] + wine[1])
    sys.exit()

dp = [0] * n

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(max(dp))

## dp 는 항상 마지막에 어떻게 되는지 생각하며 풀기


