import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,(input().strip())))) # 각각의 수들은 붙어서 입력으로 주어진다 -> strip 으로 

def bfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] == 1: # 1이면 미로 길임, queue 에 넣는다
                    queue.append((nx,ny)) 
                    graph[nx][ny] = graph[x][y] + 1 # 마지막 위치값을 반환하면 답 바로 짠

    print(graph[N - 1][M -1]) # 마지막 위치 반환

bfs(0,0) # 시작 (1,1)