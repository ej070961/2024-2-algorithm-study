import sys
input = sys.stdin.readline

N = int(input())  
matrix = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

# dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱할 때 최소 곱셈 연산 수
for length in range(1, N):  # 부분 행렬의 길이
    for i in range(N - length):
        j = i + length
        dp[i][j] = float('inf')  # 일단 아주 큰 수로 설정
        # i에서 j까지의 행렬을 곱하는데 드는 최소 비용 계산
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

# 첫번째 행렬부터 N번째 행렬까지 곱할 때의 최소 연산 횟수
print(dp[0][N - 1])
