import sys

N = int(sys.stdin.readline().strip())
T = []
P = []

for _ in range(N):
  t, p = map(int, sys.stdin.readline().strip().split(" "))
  T.append(t)
  P.append(p)

# N + 1 퇴사일까지 상담
incomes = [0 for _ in range(N + 1)]

# 날짜 0부터 N까지 임금 계산
for i in range(N):
  # 퇴사일을 포함한 그 이전까지 종료되는 상담만 계산함.
  # 날짜 i에 시작하는 상담에 대해 최대값 저장: 상담 종료일에 이미 계산된 임금 vs i일에 계산된 임금 + 상담 임금
  if i + T[i] <= N:
    incomes[i+ T[i]] = max(incomes[i + T[i]], incomes[i] + P[i])

  # 다음 날짜 임금 갱신 (일 없는 날에도 갱신 해야함)
  incomes[i + 1] = max(incomes[i + 1], incomes[i])

print(incomes[N])