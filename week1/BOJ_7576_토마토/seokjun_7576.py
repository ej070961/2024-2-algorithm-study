from collections import deque

M, N = map(int, input().split(" ")) # M은 가로길이, N은 세로길이
box = [[] for _ in range(N)]

for n in range(N):
  row = list(map(int, input().split(" ")))
  for m in range(M):
    box[n].append(row[m])

dirs = [1, -1, 0, 0, 1, -1]
def bfs(maturedPositions):
  q = deque()

  for matured in maturedPositions:
    q.append(matured)

  while q:
    position = q.popleft()
    y = position[0]
    x = position[1]
    day = box[y][x]

    for i in range(4):
      newY = y + dirs[i]
      newX = x + dirs[i + 2]

      if newY < 0 or newX < 0 or newY >= N or newX >= M or box[newY][newX] != 0:
        continue

      q.append((newY, newX))
      box[newY][newX] = day + 1

maturedPositions = []
for y in range(N):
  for x in range(M):
    if box[y][x] == 1:
      maturedPositions.append((y, x))

bfs(maturedPositions)

def getDays():
  max = -1
  for y in range(N):
    for x in range(M):
      if box[y][x] == 0:
        return -1

      if box[y][x] > max:
        max = box[y][x]

  return max - 1

print(getDays())