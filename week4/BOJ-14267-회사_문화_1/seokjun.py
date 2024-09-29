import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(" "))

# 직원의 상하 관계
workers = list(map(int, input().strip().split(" ")))

# 결과 저장할 배열, n번 직원 = n-1번째 인덱스
res = [0 for _ in range(n)]

# 칭찬 받은 직원 번호와 칭찬 정도
for i in range(m):
  i, w = map(int, input().strip().split(" "))
  res[i-1] += w

# n번 직원의 칭찬 정도는 n번 직원의 직속 상사의 칭찬 정도 + 본인이 받은 칭찬 정도
for i in range(1, n):
  res[i] = res[workers[i]-1] + res[i]

print(" ".join(map(str, res)))