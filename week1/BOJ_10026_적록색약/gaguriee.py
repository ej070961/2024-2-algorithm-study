import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

array = [list(input().strip()) for _ in range(N)]

def dfs(x, y, visited, is_color_blind):
    visited[x][y] = True
    current_color = array[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            neighbor_color = array[nx][ny]
            if (is_color_blind and current_color in 'RG' and neighbor_color in 'RG') or current_color == neighbor_color:
                dfs(nx, ny, visited, is_color_blind)

# 일반
visited = [[False] * N for _ in range(N)]
normal_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, visited, is_color_blind=False)
            normal_count += 1

# 색맹
visited = [[False] * N for _ in range(N)]
color_blind_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, visited, is_color_blind=True)
            color_blind_count += 1

print(normal_count, color_blind_count)
