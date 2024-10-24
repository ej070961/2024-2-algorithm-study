from collections import deque
import sys
input = sys.stdin.readline

# m = 가로 , n = 세로
# 1 = 익음, 0 = 익지않음, -1 = 없음
m, n = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))


queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

# 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 # 일수 저장
                queue.append([nx,ny])
# 토마토 시작
bfs()

cnt = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(line))

print(cnt - 1) # 1인 토마토 부터 시작했기에
    









