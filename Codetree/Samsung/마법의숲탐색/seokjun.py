"""
골렘을 하나씩 숲에 입장시킴
    a:
    이동 방법 1이 가능한지 확인:
        가능하면 이동 방법 1 실행 후 a로 되돌아 감.
        불가능하면 이동방법 2가 가능한지 확인:
            가능하면 이동 방법 2 실행 후 a로 되돌아 감.
            불가능하면 이동 방법 3이 가능한지 확인:
                가능하면 이동 방법 3 실행 후 a로 되돌아 감.
                불가능하면 골렘 몸이 숲 밖에 있는지 확인:
                    그렇다면 모든 골렘 삭제 후 다음 골렘으로 넘어감. 그렇지 않다면 2번으로
                    그렇지 않다면 정령 이동 실행.
    정령의 최종 위치의 행 번호를 정답에 추가.
"""

import sys
from collections import deque
readline = sys.stdin.readline

# 입력 받기
R, C, K = map(int, readline().split())
golems = [list(map(int, readline().split())) for _ in range(K)]

# 이차원 배열 숲 초기화: 0,1,2번째 행은 숲 밖임.
height = R + 3
width = C
forest = [[[0, False] for _ in range(width)] for _ in range(height)]

# 골렘 중앙 위치로부터 골렘이 중앙, 북, 동, 남, 서 차지하고 있는 위치 반환
def get_cur_golem_space(cur_position):
    curY, curX = cur_position
    return [
        (curY, curX),
        (curY - 1, curX),
        (curY, curX + 1),
        (curY + 1, curX),
        (curY, curX - 1)
    ]

def is_move1_available(cur_position):
    """
    첫번째 이동 방법이 가능한지 확인하는 함수
    Parameters:
    curPosition (tuple of (int, int)): 골렘의 중앙 좌표 (y, x)

    Returns:
    bool: 첫번째 이동 방법이 가능하면 True
    """
    cur_center, cur_north, cur_east, cur_south, cur_west = get_cur_golem_space(cur_position)
    if (
        cur_west[0] + 1 >= 0 and cur_west[0] + 1 < height and forest[cur_west[0] + 1][cur_west[1]][0] == 0 and
        cur_south[0] + 1 >= 0 and cur_south[0] + 1 < height and forest[cur_south[0] + 1][cur_south[1]][0] == 0 and
        cur_east[0] + 1 >= 0 and cur_east[0] + 1 < height and forest[cur_east[0] + 1][cur_east[1]][0] == 0
    ):
        return True
    return False

# 첫 번째 이동 실행
def move1(cur_position, cur_exit):
    """
    첫번째 이동을 실행하는 함수
    Parameters:
    curPosition (tuple of (int, int)): 골렘의 중앙 좌표 (y, x)
    """
    cur_position[0] += 1

# 두 번째 이동 방법이 가능한지 확인
def is_move2_available(cur_position):
    cur_center, cur_north, cur_east, cur_south, cur_west = get_cur_golem_space(cur_position)
    if (
        cur_north[1] - 1 >= 0 and cur_north[1] - 1 < width and forest[cur_north[0]][cur_north[1] - 1][0] == 0 and
        cur_west[1] - 1 >= 0 and cur_west[1] - 1 < width and forest[cur_west[0]][cur_west[1] - 1][0] == 0 and
        cur_south[1] - 1 >= 0 and cur_south[1] - 1 < width and forest[cur_south[0]][cur_south[1] - 1][0] == 0 and
        cur_west[0] + 1 >= 0 and cur_west[0] + 1 < height and forest[cur_west[0] + 1][cur_west[1] - 1][0] == 0 and
        cur_south[0] + 1 >= 0 and cur_south[0] + 1 < height and forest[cur_south[0] + 1][cur_south[1] - 1][0] == 0
    ):
        return True
    return False

# 두 번째 이동 실행
def move2(cur_position, cur_exit):
    cur_position[0] += 1
    cur_position[1] -= 1
    return cur_exit - 1 if cur_exit != 0 else 3

# 세 번째 이동 방법이 가능한지 확인
def is_move3_available(cur_position):
    cur_center, cur_north, cur_east, cur_south, cur_west = get_cur_golem_space(cur_position)
    if (
        cur_north[1] + 1 >= 0 and cur_north[1] + 1 < width and forest[cur_north[0]][cur_north[1] + 1][0] == 0 and
        cur_east[1] + 1 >= 0 and cur_east[1] + 1 < width and forest[cur_east[0]][cur_east[1] + 1][0] == 0 and
        cur_south[1] + 1 >= 0 and cur_south[1] + 1 < width and forest[cur_south[0]][cur_south[1] + 1][0] == 0 and
        cur_east[0] + 1 >= 0 and cur_east[0] + 1 < height and forest[cur_east[0] + 1][cur_east[1] + 1][0] == 0 and
        cur_south[0] + 1 >= 0 and cur_south[0] + 1 < height and forest[cur_south[0] + 1][cur_south[1] + 1][0] == 0
    ):
        return True
    return False

# 세 번째 이동 실행
def move3(cur_position, cur_exit):
    cur_position[0] += 1
    cur_position[1] += 1
    return cur_exit + 1 if cur_exit != 3 else 0

# 골렘이 숲 밖에 있는지 확인
def is_golem_outside(cur_position):
    if cur_position[0] - 1 < 3:
        return True
    return False

# 숲 초기화
def clear_forest():
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            forest[i][j] = [0, False]

# 골렘 고정
def fix_golem(cur_position, cur_exit, golem_number):
    golem_space = get_cur_golem_space(cur_position)
    for i in range(len(golem_space)):
        y, x = golem_space[i]
        forest[y][x][0] = golem_number
        if i == cur_exit + 1:
            forest[y][x][1] = True

# 정령 이동
y_dirs = [1, 0, -1, 0]
x_dirs = [0, 1, 0, -1]

def move_soul_to_bottom(soul_position):
    visited = [[False for _ in range(width)] for _ in range(height)]
    q = deque()
    q.append(soul_position)
    visited[soul_position[0]][soul_position[1]] = True

    while q:
        curY, curX = q.pop()
        cur_golem_number, cur_is_exit = forest[curY][curX]

        for d in range(4):
            nextY, nextX = curY + y_dirs[d], curX + x_dirs[d]

            if nextY < 0 or nextY >= height or nextX < 0 or nextX >= width or visited[nextY][nextX]:
                continue

            next_golem_number, next_is_exit = forest[nextY][nextX]

            if next_golem_number == 0:
                continue

            if cur_golem_number == next_golem_number:
                q.append((nextY, nextX))
                visited[nextY][nextX] = True
            elif cur_is_exit:
                q.append((nextY, nextX))
                visited[nextY][nextX] = True

    for i in range(len(visited) - 1, 2, -1):
        if True in visited[i]:
            return i - 3 + 1

# 메인 로직
answer = 0
for i in range(1, K + 1):
    c, d = golems[i - 1]
    cur_position = [1, c - 1]
    soul_position = cur_position
    cur_exit = d
    final_soul_row = 0

    while True:
        if is_move1_available(cur_position):
            move1(cur_position, cur_exit)
        elif is_move2_available(cur_position):
            cur_exit = move2(cur_position, cur_exit)
        elif is_move3_available(cur_position):
            cur_exit = move3(cur_position, cur_exit)
        elif is_golem_outside(cur_position):
            clear_forest()
            break
        else:
            soul_position = cur_position
            fix_golem(cur_position, cur_exit, i)
            final_soul_row = move_soul_to_bottom(soul_position)
            break

    answer += final_soul_row

print(answer)
