import sys
from collections import deque


input = sys.stdin.readline

#상자의 가로 칸의 수, 세로 칸의 수 입력받기
M, N = map(int, input().split())

#그래프 초기화 
graph = [[] for _ in range(N)]

#토마토 정보 세팅
#익은 토마토 1
#익지않은 토마토 0
#토마토가 들어있지 않은 칸 -1 
for i in range(N):
    graph[i] = list(map(int, input().split()))


q = deque([])
for i in range(N):
    for j in range(M):
        #익어있는 토마토를 만났다면 
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < N and 0 <= ny < M:
            #인접한 토마토가 0
            if graph[nx][ny] == 0 :
                #이전 지점보다 값을 1 증가 -> 날짜 카운팅 용도 
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


max_count = 0
for i in range(N):
    for j in range(M):
        #0이 남아 있을 경우
        if graph[i][j] == 0:
            print(-1)
            exit()

        if graph[i][j]-1 > max_count:
            max_count = graph[i][j] -1 

print(max_count)