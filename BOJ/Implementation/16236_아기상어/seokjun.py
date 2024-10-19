from collections import deque

N = int(input())
global sea
global curSize
global curFeed 
sea = [] 
curSize = 2 # 상어 크기
curFeed = 0 # 먹은 양

position = (0,0) # 상어 위치
time = 0 # 이동 시간

# sea 초기화
for n in range(N):
  sea.append(list(map(int, input().split(" "))))
  # 초기 상어 위치 초기화
  if 9 in sea[n]:
    position = (n, sea[n].index(9))
    sea[n][position[1]] = 0

# 현재 상어 위치에서 모든 칸까지 거리 반환하는 함수
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
def getDistances(position):
  global curSize
  distances = [[-1] * N for _ in range(N)]
  q = deque()
  q.append(position)
  distances[position[0]][position[1]] = 0

  while q:
    y, x = q.popleft()
    for k in range(4):
      newY = y + dy[k]
      newX = x + dx[k]
      if 0 <= newY < N and 0 <= newX < N: # 바다 범위 내
        if (
          distances[newY][newX] == -1 and # 미방문한 경우
          sea[newY][newX] <= curSize # 물고기가 있으면 지나가거나 먹을 수 있는 경우
        ):
          q.append((newY, newX))
          distances[newY][newX] = distances[y][x] + 1

  return distances

# 먹은 물고기 수를 확인하고 상어 크기를 키우는 함수
def sizeUp():
  global curSize
  global curFeed
  curFeed += 1
  if curFeed == curSize:
    curSize += 1
    curFeed = 0

# 가장 가까운 먹이 찾는 함수
def findNearestFish(distances):
  global sea
  global curSize
  minDist = float('inf')
  fishList = []

  # 위쪽, 왼쪽부터 탐색
  for i in range(N):
    for j in range(N):
      if (
        sea[i][j] > 0 and # 물고기가 존재하는 경우
        sea[i][j] < curSize and # 먹을 수 있는 크기인 경우
        distances[i][j] != -1 # 이동 가능한 칸인 경우
        ):
        dist = distances[i][j]
        if dist < minDist:
          minDist = dist
          fishList.clear()
          fishList = [(i, j)]
        elif dist == minDist:
          fishList.append((i, j))
  
  if not fishList:
    return 0
  
  return fishList[0]

while True:
  """
  먹을 수 있는 물고기와 그 거리를 구함.
  """
  distances = getDistances(position)
  nextFish = findNearestFish(distances)

  """
  먹을 수 있는 물고기가 없으면
  종료
  """
  if nextFish == 0:
    break

  """
  먹을 수 있는 물고기가 있으면
  최종 시간 더해주고, 상어 위치 옮겨주고, 먹은 물고기 삭제하고, 상어 크기 키움.
  """ 
  y, x = nextFish
  time += distances[y][x]
  position = (y, x)
  sea[y][x] = 0
  sizeUp()

print(time)
