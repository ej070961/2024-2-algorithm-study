import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = []
max_h = 0
result = 0



for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] > max_h:
            max_h = graph[i][j] # 최대 높이 구하기

dx = [0,0,1,-1]
dy = [1,-1,0,0] # 상하좌우

def dfs(x, y, h):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] == 1:
            if graph[nx][ny] > h:
                visited[nx][ny] = 1 # 방문 처리
                dfs(nx,ny,h) 

for i in range(max_h):
    visited = [[0] * n for _ in range(n)] # visited 0 세팅
    cnt = 0 # 안전영역 수

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                dfs(j,k,i)
                cnt += 1
    result = max(result, cnt)

print(result)




