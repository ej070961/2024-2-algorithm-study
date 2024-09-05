import sys

sys.setrecursionlimit(100000)

def dfs(h, x, y):
    visited[x][y] = 1
    for dx, dy in [(1, 0), (-1, 0),(0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
         if visited[nx][ny] == 0 and graph[nx][ny] > h:
            dfs(h, nx, ny)


input = sys.stdin.readline

#행과 열 개수 입력 받기
N = int(input())

#그래프 초기화
graph = [[]for _  in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split(' ')))

#모두 잠기는 최대 높이 
max_height = max(max(row) for row in graph)
ans = [0] * (max_height + 1)
ans[max_height] = 0


#높이를 증가시키면서 안전영역 개수 구하기 
for h in range(0, max_height):
    count = 0
    visited = [[0 for _  in range(N)] for _  in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and graph[x][y] > h:
                  count += 1
                  dfs(h, x, y)
    ans[h] = count
    
# print(ans)
print(max(ans))