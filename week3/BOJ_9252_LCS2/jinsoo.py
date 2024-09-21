import sys

input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())

len1 = len(str1)
len2 = len(str2)

dp = [[''] * (len2+1) for _ in range(len1+1)]

# print(str1)
# print(str2)
# print(dp)

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])