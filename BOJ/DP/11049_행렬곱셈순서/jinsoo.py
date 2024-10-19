import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
# print(matrix)
for i in range(n-1):
    dp[i][i+1] = matrix[i][0] * matrix[i+1][0] * matrix[i+1][1]
# print(dp)

for length in range(2,n): # 길이가 2 이상인 구간에 대한 dp 계산
    for i in range(n-length): # length 는 현재 구간의 길이 (행렬 개수)
        j = i + length # 끝 행렬 인덱스
        dp[i][j] = 2**31
        for k in range(i,j):
            cost = dp[i][k] + dp[k+1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1])
            dp[i][j] = min(dp[i][j], cost)
            
# print(dp)
print(dp[0][n-1])
