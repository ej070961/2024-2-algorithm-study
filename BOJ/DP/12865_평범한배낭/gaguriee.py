import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])

for i in range(1, N + 1):
  for j in range(1, K + 1):
    weight = bag[i][0]
    value = bag[i][1]

    # i번째 아이템의 무게가 
    # 가방의 최대 한도 j(kg)를 초과했을 경우
    if j < weight :
        dp[i][j] = dp[i-1][j]
    
    # 초과하지 않았을 경우
    # i번째 아이템을 포함시켰을 경우와, 포함하지 않았을 경우 중 최대 가치를 저장
    else :
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
    

print(dp[N][K])
