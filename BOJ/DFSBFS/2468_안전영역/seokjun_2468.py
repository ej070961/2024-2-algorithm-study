import sys
sys.setrecursionlimit(10**6)

N = int(input())

# 입력값을 field에 저장
field = [[] for _ in range(N)]
maxHeight = -1
for i in range(N):
  row = input().split(" ")
  for j in range(N):
    height = int(row[j])
    field[i].append(height)
    # 최고 높이 셀 업데이트
    if height > maxHeight:
      maxHeight = height

# 입력: field (땅의 높이) => 반환: newField (땅의 안전 여부)
def rainField(rain):
  newField = [[1]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if field[i][j] <= rain:
        newField[i][j] = 0
  return newField

dirs = [1, -1, 0, 0, 1, -1]
def dfs(board, x, y):
  board[x][y] = 0

  for i in range(4):
    newX = x + dirs[i]
    newY = y + dirs[i+2]
    if newX < 0 or newY < 0 or newX >= N or newY >= N or board[newX][newY] == 0:
      continue
    dfs(board, newX, newY)

maxSafeArea = -1

for rain in range(maxHeight):
  fieldAfterRain = rainField(rain)
  safeArea = 0

  for i in range(N):
    for j in range(N):
      if fieldAfterRain[i][j] == 1:
        dfs(fieldAfterRain, i, j)
        safeArea += 1

  if safeArea > maxSafeArea:
    maxSafeArea = safeArea

print(maxSafeArea)
