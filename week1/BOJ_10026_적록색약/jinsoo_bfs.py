from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)] 
# graph = [list(input().strip() for _ in range(n))]
# 이렇게 적어서 오류 찾는 시간이 오래 걸렷음 ㅜ
# print(graph)
visited = [[0] * n for _ in range(n)]
answer = [0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                
# 적록색맹 x 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answer[0] += 1
# 적록색맹 o
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answer[1] += 1

print(' '.join(map(str, answer)))
