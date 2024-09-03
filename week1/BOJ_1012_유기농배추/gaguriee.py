import sys
sys.setrecursionlimit(10**6)

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if arr[nx][ny] == 1:
                dfs(nx, ny)
            else:
                visited[nx][ny] = True

input = sys.stdin.readline
t = int(input())
answers = []

for _ in range(t):
    n, m, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    answers.append(cnt)

print(*answers, sep='\n')
