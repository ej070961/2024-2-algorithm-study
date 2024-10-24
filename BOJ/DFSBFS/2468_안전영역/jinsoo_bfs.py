# bfs 풀이
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
max_h = 0

for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

    for i in row:
        if i > max_h:
            max_h = i

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,h):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > h and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    

result = []

for i in range(max_h):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i)
                cnt += 1
    result.append(cnt)

print(max(result))


