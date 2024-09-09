import sys

def dfs(color, visited, i, j):
    stack = [(i, j)]

    while stack:
        x, y = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny] in color:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

input = sys.stdin.readline

#N을 입력받음
N = int(input())

#그래프 초기화 
graph = [[] for _ in range(N)]

common_visited = [[False for _ in range(N) ] for _ in range(N)]
unique_visited = [[False for _ in range(N) ] for _ in range(N)]

#일반인이 보는 구역 수
common = 0
#적록색약이 보는 구역 수 
unique = 0

for i in range(N):
    graph[i] = input().rstrip()

# print(graph)
for i in range(N):
    for j in range(N):
        if  not common_visited[i][j]:
            common_visited[i][j] = True
            common+= 1
            if graph[i][j] == 'R':
                dfs('R', common_visited, i, j)
            elif graph[i][j] == 'G':
                dfs('G', common_visited, i, j)
            else:
                dfs('B', common_visited, i, j)

# print(common)


for i in range(N):
    for j in range(N):
        if  not unique_visited[i][j]:
            unique_visited[i][j] = True
            unique+= 1
            if graph[i][j] == 'R' or  graph[i][j] == 'G':
         
                dfs(['R', 'G'], unique_visited, i, j)
            else:

                dfs('B', unique_visited, i, j)

print(common, unique)