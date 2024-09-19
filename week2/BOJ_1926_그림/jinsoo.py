import sys
from collections import deque

input = sys.stdin.readline

n , m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))



def bfs(x,y):
    width = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 # start 지점 visited 처리 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0 # visited 처리
                    queue.append((nx,ny))
                    width += 1
    return width

cnt = 0
canvas = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            canvas = max(bfs(i,j),canvas)

print(cnt)
print(canvas)
        