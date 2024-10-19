import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split()) 
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

arr = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def dfs(x,y, cnt):
    global area

    area[cnt] = area[cnt] + 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == False :
            dfs(nx,ny, cnt)

cnt = 0
area = [0] * (N * M) # 각 그림 별 넓이 저장, 최대로 생성 가능한 그림의 수 N * M 개

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == False :
            cnt = cnt + 1
            dfs(i, j, cnt)

print(cnt)
print(max(area))
