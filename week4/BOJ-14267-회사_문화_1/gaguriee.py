import sys
input = sys.stdin.readline

# 회사의 직원 수 n명, 최초의 칭찬의 횟수 m
N, M = map(int, input().split())

# 직원 n명의 직속 상사의 번호 (boss[i]는 i번의 상사 번호)
boss = [0] + list(map(int, input().split())) 

# 직원별 칭찬 횟수
dp = [0] * (N+1)

# 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
for _ in range(M):
    i, w = map(int, input().split())
    dp[i] = dp[i] + w

for i in range(2,N+1,1):
    # 직속상사의 내리칭찬
    dp[i] = dp[boss[i]] + dp[i]

# 0번째 인덱스 제외
print(" ".join(map(str, dp[1:])))
