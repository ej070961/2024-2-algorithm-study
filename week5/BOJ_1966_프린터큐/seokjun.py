import sys
from collections import deque
readline = sys.stdin.readline

T = int(readline())
result = []

# 큐의 첫번째 원소의 우선순위가 가장 큰지 확인하는 함수
def isMaxAtFirst(queue):
  targetPriority, _ = queue[0]
  
  return len(list(filter(lambda e: e[0] > targetPriority, queue))) == 0

for _ in range(T):
  N, M = map(int, readline().split(" "))
  priorities = list(map(int, readline().split(" ")))
  
  # 인쇄 순서를 알고 싶은 목표 문서를 표시해주기 위해 배열 수정.
  # 우선순위 배열: [4, 1, 3] => (우선순위, 목표값 여부 0 or 1) 배열: [(4,0), (1,1), (3,0)]
  q = deque([(val, 1) if idx == M else (val, 0) for idx, val in enumerate(priorities)])
  cnt = 0

  while True:
    # 첫번째 원소의 우선순위가 가장 큰 경우, 첫번째 원소를 제거함.
    if isMaxAtFirst(q):
      _, isTarget = q.popleft()
      cnt += 1
      # 제거된 원소가 목표 문서라면 반복을 종료함.
      if isTarget:
        break
    # 첫번째 원소보다 우선순위가 큰 원소가 존재하는 경우, 첫번째 원소를 맨 뒤로 옮김.
    else:
      item = q.popleft()
      q.append(item)

  result.append(cnt)
  
print("\n".join(map(str, result)))