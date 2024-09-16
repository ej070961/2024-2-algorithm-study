from collections import deque

# 입력 받기: N, M, maze
firstLine = list(map(int, input().split(" ")))
N = firstLine[0]
M = firstLine[1]
maze = []

# 방문 여부와 지나간 칸 수 저장할 배열 초기화
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
  maze.append(list(map(int, input())))

# 이동 방향 저장하는 배열 초기화
dirs = [1, -1, 0, 0, 1, -1]

def bfs():
  q = deque()
  q.append((0,0))
  visited[0][0] = 1
  
  while q:
    curY, curX = q.popleft()

    for i in range(4):
      newY = curY + dirs[i]
      newX = curX + dirs[i+2]

      # 인접한 칸이 이동 불가한 칸 또는 이미 방문한 칸이면 이동하지 않음.
      if (
        not (0 <= newY < N) or not (0 <= newX < M) or
        maze[newY][newX] == 0 or
        visited[newY][newX] > 0
      ):
        continue

      q.append((newY, newX))
      # 인접 칸의 지나온 칸 수 = 현재 칸의 지나온 칸 수 + 1
      visited[newY][newX] = visited[curY][curX] + 1

bfs()
print(visited[N-1][M-1])
