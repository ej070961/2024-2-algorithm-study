import sys
from collections import deque

input = sys.stdin.readline 

M, N = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                q.append((i, j, 0)) 
                visited[i][j] = True

    if len(q) == 0 :
        return 0

    while q:
        x, y, day = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and array[nx][ny] == 0: 
                q.append((nx, ny, day + 1)) # 토마토 익히기
                visited[nx][ny] = True 
                array[nx][ny] = 1
    return day

ans = bfs()

# 안 익은 토마토 있으면 -1 출력
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            print(-1)
            sys.exit()

print(ans)
