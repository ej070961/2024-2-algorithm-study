import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, shark, ans):
    q = deque([(i, j)])
    last = []
    while q:
        cur_x, cur_y = q.popleft()
        print(q)
        # 가까운 거리 탐색, 상, 좌를 우선순위로 넣기 
        for dx, dy in [(1, 0), (0, 1), (-1, 0),(0, -1)]:
            x = cur_x + dx
            y = cur_y + dy
            if 0 <= x < N and 0 <= y < N:
                if graph[x][y] == 0 or graph[x][y] == shark:
                    # graph[x][y] = -1
                    ans[x][y] = ans[cur_x][cur_y] + 1
                    q.append((x, y))
                elif graph[x][y] > 0  and graph[x][y] < shark:
                    #물고기 먹음
                    graph[x][y] = -1
                    ans[x][y] = ans[cur_x][cur_y] + 1
                    shark += 1
                    last = (x, y)
                    q.append((x, y))
                    continue

    return last
N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]


#초기 상어의 크기 
shark = 2
for i in range(N):
    graph[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            last = bfs(i, j , shark, ans)


print(ans[last[0]][last[1]] if len(last)>0 else 0)
 
