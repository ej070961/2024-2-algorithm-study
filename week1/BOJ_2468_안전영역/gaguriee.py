import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())

arr = []

for _ in range(N) :
    row = list(map(int, input().split()))
    arr.append(row)

max_value = max(max(row) for row in arr)
min_value = min(min(row) for row in arr)


def dfs(x, y, height):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if arr[nx][ny] >= height:
                dfs(nx, ny, height)
            else:
                visited[nx][ny] = True

answers = []

for height in range(min_value, max_value+1, 1):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] >= height and not visited[x][y]:
                cnt += 1
                dfs(x, y, height)

    answers.append(cnt)


print(max(answers))
