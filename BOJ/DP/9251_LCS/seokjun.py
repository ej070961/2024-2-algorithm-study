import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
l1 = len(s1)
l2 = len(s2)

# dp[i][j]: s1의 i번째 문자와 s2의 j번째 문자까지 확인했을 때 LCS의 길이

dp = list([0] * (l2 + 1) for _ in range(l1 + 1))

for i in range(1, l1+1):
  for j in range(1, l2+1):
    if s1[i-1] == s2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[l1][l2])