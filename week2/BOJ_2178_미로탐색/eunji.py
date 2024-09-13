import sys
from collections import deque

input = sys.stdin.readline

INF = float('inf')

def bfs(i, j):

    q = deque([(i, j)])

    while q:
        # print(q)
        cur_x, cur_y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = cur_x + dx
            y = cur_y + dy

            #범위 체크
            if 0 <= x < N and 0 <= y < M:
                # 처음 지나갈 수 있는 칸이거나, 비용이 저장된 비용보다 작을 때 (더 적은 비용으로 갈 수 있을 때)
                if graph[x][y] == 1 or graph[cur_x][cur_y] + 1 < graph[x][y]:
                    graph[x][y] = graph[cur_x][cur_y] + 1
                    q.append((x,y))


# N, M 입력받기
N, M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    str = input().rstrip()
    for j in range(M):
        graph[i][j] = int(str[j])

bfs(0,0)

print(graph[N-1][M-1])