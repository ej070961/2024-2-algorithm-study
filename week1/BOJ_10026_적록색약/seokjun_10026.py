from collections import deque

N = int(input())
picture = []

for i in range(N):
  row = list(input())
  picture.append(row)

normal = 0
abnormal = 0
visitedNormal = [[False for _ in range(N)] for _ in range(N)]
visitedAbnormal = [[False for _ in range(N)] for _ in range(N)]

dirs = [1, -1, 0, 0, 1, -1]

def bfsNormal(i ,j):
  q = deque()
  q.append((i, j))
  visitedNormal[i][j] = True

  while(q):
    cell = q.popleft()
    y = cell[0]
    x = cell[1]
    currentColor = picture[y][x]

    for k in range(4):
      newY = y + dirs[k]
      newX = x + dirs[k+2]

      if (
        newY < 0 or newX < 0 or 
        newY >= N or newX >= N or 
        visitedNormal[newY][newX] or
        currentColor != picture[newY][newX]):
        continue

      q.append((newY, newX))
      visitedNormal[newY][newX] = True;

def bfsAbnormal(i ,j):
  def isSameColor(a, b):
    if (a == b or (a == "R" and b == "G") or (a == "G" and b == "R")):
      return True
    else:
      return False
  
  q = deque()
  q.append((i, j))
  visitedAbnormal[i][j] = True

  while(q):
    cell = q.popleft()
    y = cell[0]
    x = cell[1]
    currentColor = picture[y][x]

    for k in range(4):
      newY = y + dirs[k]
      newX = x + dirs[k+2]

      if (
        newY < 0 or newX < 0 or 
        newY >= N or newX >= N or 
        visitedAbnormal[newY][newX] or
        not isSameColor(currentColor, picture[newY][newX])):
        continue

      q.append((newY, newX))
      visitedAbnormal[newY][newX] = True

for i in range(N):
  for j in range(N):
    if not visitedNormal[i][j]:
      bfsNormal(i, j)
      normal += 1
  
for i in range(N):
  for j in range(N):
    if not visitedAbnormal[i][j]:
      bfsAbnormal(i, j)
      abnormal += 1

print(f'{normal} {abnormal}')
