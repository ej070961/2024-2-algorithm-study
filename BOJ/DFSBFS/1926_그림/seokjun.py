import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split(" ")))
paper = []
visited = [[False] * m for _ in range(n)]
numOfPictures = 0
global curPictureSize 
curPictureSize = 0
maxPictureSize = 0

for _ in range(n):
  paper.append(list(map(int, input().split(" "))))

dirs = [1, -1, 0, 0, 1, -1]
def dfs(y, x):
  visited[y][x] = True
  global curPictureSize 
  curPictureSize += 1
  for i in range(4):
    newY, newX = y + dirs[i], x + dirs[i+2]

    if 0 <= newY < n and 0 <= newX < m and not visited[newY][newX] and paper[newY][newX] == 1:
      dfs(newY, newX)

for i in range(n):
  for j in range(m):
    if not visited[i][j] and paper[i][j] == 1:
      numOfPictures += 1
      dfs(i, j)
      if curPictureSize > maxPictureSize:
        maxPictureSize = curPictureSize
      curPictureSize = 0

print(numOfPictures)
print(maxPictureSize)


