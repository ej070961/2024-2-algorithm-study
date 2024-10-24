from collections import deque
import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
maze = [list(map(int, input().strip().split())) for _ in range(N)]

# 아기 상어 초기 정보
pos_x, pos_y = next((i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 9)
maze[pos_x][pos_y] = 0
size = 2
remainder = 2  # 아기 상어가 다음 크기로 커지기 위해 필요한 물고기 수

# 방향 벡터
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(start_x, start_y):
    # BFS 탐색
    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[start_x][start_y] = True
    fish = []  # 먹을 수 있는 물고기들

    min_dist = sys.maxsize
    while queue:
        x, y, dist = queue.popleft()

        if 0 < maze[x][y] < size:
            # 먹을 수 있는 물고기 발견 시 리스트에 추가
            if dist <= min_dist:
                min_dist = dist
                fish.append((dist, x, y))
        
        # BFS 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] <= size:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 조건에 맞는 물고기 선택
    if fish:
        fish.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, x좌표, y좌표 순으로 정렬
        return fish[0]
    else:
        return None

time = 0  # 총 시간
while True:
    target = bfs(pos_x, pos_y)

    if target is None:
        break  # 더 이상 먹을 수 있는 물고기가 없으면 종료

    # 물고기를 먹고 상어의 위치 갱신
    dist, new_x, new_y = target
    pos_x, pos_y = new_x, new_y
    maze[pos_x][pos_y] = 0  # 먹은 물고기 처리
    time += dist

    # 상어 성장 처리
    remainder -= 1
    if remainder == 0:
        size += 1
        remainder = size

# 결과 출력
print(time)
