import sys

input = sys.stdin.readline

n, m = map(int, input().split())

employee = [0] * (n+1) 

# 상사 번호 입력 받기
supervisors = list(map(int, input().split()))

for i in range(1, n):
    employee[i + 1] = supervisors[i]

# i 번호를 가진 직원이 받은 칭찬의 정도 
dp = [0] * (n+1)

for _ in range(m):
    # 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
    i, w = map(int, input().split())
    dp[i] += w #이부분 때문에 계속 틀림 


for i in range(2, n+1):
    #직속상사가 칭찬한 정도 + 직속상사가 받은 칭찬의 정도 
    dp[i] += dp[employee[i]] 


# 결과 출력
print(' '.join(map(str, dp[1:])))
