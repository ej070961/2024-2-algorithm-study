import sys

input = sys.stdin.readline

INF = float('inf')
#행렬의 개수
N = int(input())

#행렬 크기 리스트 초기화
matrics = []

#행렬크기 입력받기 
for  _ in range(N):
    r, c = map(int, input().split())
    matrics.append((r,c))

#DP 테이블 초기화 (N x N)
#dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱하는 데 필요한 최소 연산 횟수 
dp = [[0]*N for _ in range(N)]

#행렬곱셈순서 계산
for length in range(1, N): #부분 문제의 길이, 즉 한번에 몇 개의 행렬을 곱하는지
    for i in range(N-length): #시작하는 행렬 인덱스
        j = i + length #끝나는 행렬 인덱스
        dp[i][j] = INF # 매우 큰 값으로 초기화

        #i, j 사이 구간을 나누는 k를 반복 
        for k in range(i, j):
            #i~k 행렬과 k+1~j행렬을 곱한후, 그 둘의 곱하는 연산 수를 계산함
            cost =  dp[i][k] + dp[k+1][j] + matrics[i][0] * matrics[k][1] * matrics[j][1]
            #최솟값을 계속 갱신 
            dp[i][j] = min(dp[i][j], cost)

# 결과 출력 (1번째 행렬부터 N번째 행렬까지 곱하는데 필요한 최소 연산 수)
print(dp[0][N-1])