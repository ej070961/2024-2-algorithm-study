from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1: # 이동할 수  있는 칸이면서, 방문한 적 없는 칸일 경우
                
                maze[nx][ny] = maze[x][y] + 1 # 새로운 칸을 방문하여 이전 칸의 거리 + 1
                queue.append((nx, ny))

    # 도착 지점의 거리 반환
    return maze[N-1][M-1]

print(bfs(0, 0))