"""
한 배추에 위치한 한 마리 이상의 지렁이는 상하좌우 인접한 배추 보호 가능
격자에 군데군데 배추가 심어져 있을 때, 모든 배추 커버하는 지렁이 최소 수
"""
from collections import deque

def bfs(width, depth, field, visited):
  q = deque()
  dirs = [0, 0, 1, -1, 0, 0] # 이동 방향 담은 배열
  worm_count = 0

  for i in range(depth):
    for j in range(width):
      if field[i][j] == 1 and not visited[i][j]:
        q.append([i, j])
        visited[i][j] = True
        worm_count += 1

        while q:
          cur = q.popleft()
          for k in range(len(dirs)-2):
            new_y = cur[0] + dirs[k]
            new_x = cur[1] + dirs[k + 2]
            if 0 <= new_y < depth and 0 <= new_x < width:
                if field[new_y][new_x] == 1 and not visited[new_y][new_x]:
                    visited[new_y][new_x] = True
                    q.append([new_y, new_x])
  return worm_count

result = [] # 결과 담을 배열
T = int(input())

for _ in range(T):
  width, depth, numOfBaechu = map(int, input().split(" "))
  field = [[0]*width for _ in range(depth)]
  visited = [[False]*width for _ in range(depth)]

  for j in range(numOfBaechu):
    x, y = map(int, input().split(" "))
    field[y][x] = 1

  result.append(bfs(width, depth, field, visited))


for item in result:
  print(item)





