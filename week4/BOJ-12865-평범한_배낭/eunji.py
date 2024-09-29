import sys

input = sys.stdin.readline

#물품의 수, 버틸 수 있는 무게 입력
N, K = map(int, input().split())

#bag [무게, 가치] 세팅 
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]:  #현재 무게j가 해당물건무게보다 큰 경우
        #[누적된 가치 값]과 [현재물건의V+(견댈 수 있는 무게 - 현재 물건의 W)의 V]의 최댓값을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
        else:
        	#현재 견딜 수 있는 최대무게j가 해당물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            dp[i][j] = dp[i-1][j]

print(dp[N][K])  #모든 물건을 다 고려했을 때 견딜 수 있는 무게 K 최대 가치 출력 


