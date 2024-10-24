import sys
readline = sys.stdin.readline

N = int(readline())
wine = []

for _ in range(N):
  wine.append(int(readline()))

def solve(n):
  if n == 1:
    return wine[0]
  if n == 2:
    return wine[0] + wine[1]
  
  dp = [[0, 0] for _ in range(N)]
  dp[0][0] = wine[0]
  dp[0][1] = wine[0]
  dp[1][0] = wine[1]
  dp[1][1] = wine[0] + wine[1]

  # dp[k]: 0 ~ k번 와인 중 k번째 와인 먹었을 떄 최대 양.
  # dp[k][0]: k-1번 와인 선택 x, oxo 또는 oxxo 
  # dp[k][1]: k-1번 와인 선택 O, xoo

  for i in range(2, n):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1], dp[i-3][0], dp[i-3][1]) + wine[i]
    dp[i][1] = dp[i-1][0] + wine[i]
  
  return max(map(lambda v: max(v[0], v[1]), dp))

print(solve(N))