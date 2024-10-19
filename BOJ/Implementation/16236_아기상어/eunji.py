import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, shark_size):
    # 방문 배열 및 상어 이동 거리 배열 초기화
    visited = [[-1] * N for _ in range(N)]
    visited[i][j] = 0

    q = deque([(i, j)])
    fishes = []

    while q:
        cur_x, cur_y = q.popleft()

        # 상, 좌, 하, 우 순서대로 탐색
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x = cur_x + dx
            y = cur_y + dy

            if 0 <= x < N and 0 <= y < N and visited[x][y] == -1:
                # 상어가 지나갈 수 있는 칸
                if graph[x][y] <= shark_size:
                    visited[x][y] = visited[cur_x][cur_y] + 1
                    q.append((x, y))

                    # 상어가 먹을 수 있는 물고기 발견 (크기가 작은 물고기)
                    if 0 < graph[x][y] < shark_size:
                        fishes.append((visited[x][y], x, y))

    # 먹을 수 있는 물고기 중 가장 가까운, 위쪽, 왼쪽에 있는 물고기를 선택
    fishes.sort()
    if fishes:
        return fishes[0]  # 거리, x좌표, y좌표 순으로 정렬되어 있으므로 가장 우선 물고기 반환
    else:
        return None  # 먹을 수 있는 물고기가 없음


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 초기 상어의 크기와 위치
shark_size = 2
shark_x, shark_y = 0, 0

# 상어의 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0  # 상어의 시작 위치를 빈 칸으로 설정

time = 0
ate_fish = 0

# BFS 반복해서 상어가 먹을 수 있을 때까지 반복
while True:
    result = bfs(shark_x, shark_y, shark_size)
    
    # 더 이상 먹을 수 있는 물고기가 없을 경우 종료
    if result is None:
        break
    
    # 상어가 물고기를 먹고 이동
    dist, fish_x, fish_y = result
    shark_x, shark_y = fish_x, fish_y
    graph[shark_x][shark_y] = 0  # 물고기를 먹은 자리는 빈 칸으로

    time += dist  # 이동하는 시간 누적
    ate_fish += 1  # 먹은 물고기 수 증가

    # 상어가 자신의 크기만큼 물고기를 먹으면 크기 증가
    if ate_fish == shark_size:
        shark_size += 1
        ate_fish = 0

# 총 소요 시간 출력
print(time)

