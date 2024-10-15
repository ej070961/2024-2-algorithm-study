import sys
import copy
from collections import deque 
input = sys.stdin.readline

#탐사의 반복 횟수 K, 벽면에 적힌 유물 조각의 개수 M
K, M = map(int, input().split())

#유적지 배열 초기화 
arr = [list(map(int, input().split())) for _ in range(5)]

#벽면에 적힌 M개의 유물 조각 번호 저장
wall = deque(list(map(int, input().split())))


def spin_90(ci, cj, arr):
    new_arr = copy.deepcopy(arr)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_arr[ci+j][cj-i] = arr[ci+i][ci+j]
            
    return new_arr

def spin_180(ci, cj, arr):
    new_arr = copy.deepcopy(arr)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_arr[ci-i][cj-j] = arr[ci+i][ci+j]
            
    return new_arr

def spin_270(ci, cj, arr):
    new_arr = copy.deepcopy(arr)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_arr[ci-j][cj+i] = arr[ci+i][ci+j]
            
    return new_arr


def bfs (si, sj, arr, num):
    q = deque([(si, sj)])
    cnt = 0
    new_arr = copy.deepcopy(arr)
    while q:
        i, j = q.popleft()
        #유물 발굴 표시 -> 0
        new_arr[i][j] = 0
        cnt += 1
        #유물 상하좌우 체크 
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + di
            nj = j + dj
            #범위 체크 
            if 0 <= ni < 5 and 0 <= nj < 5:
                #유물의 숫자와 같은지 체크 
                if new_arr[ni][nj] == num:
                    q.append((ni, nj))
 
    return new_arr, cnt 

                

total_cnt = []
temp_arr = []
#K번의 턴에 거쳐 탐사 진행~유물 연쇄 획득
for _ in range(K):
    #1. 가능한 모든 3x3 격자에 대해 90도, 180도, 270도 회전
    #2. 회전한 각도가 작은 방법부터 실행
    #3. 회전 중심 좌표의 열, 행이 작은 순서 대로 진행 
    total_max_cnt = 0
    for i in range(1, 4):
        for j in range(1, 4):
            #90도 회전 
            new_90_arr = spin_90(i, j, arr)
            # 유물 가치 카운트 시작 
            cnt = 0
            for x in range(5):
                for y in range(5):
                    if new_90_arr[x][y] > 0:
                        result_arr, result_cnt = bfs(x, y, new_90_arr, new_90_arr[x][y])
                        #조각이 3개 이상 연결된 경우, 유물이 되고 사라짐 
                        if result_cnt >= 3:
                            new_90_arr = result_arr
                            cnt += result_cnt
                            # print(new_90_arr)
                            # print(cnt)

            #만약 유물 가치 합이 현재 최댓값보다 크면 임시 배열에 현재 회전한 배열 저장 
            if cnt > total_max_cnt:
                temp_arr = new_90_arr

                # print(temp_arr)
                total_max_cnt = cnt
                


    # print(temp_arr)
                
    for i in range(1, 4):
        for j in range(1, 4):
            cnt = 0
            new_180_arr = spin_180(i, j, arr)
            for x in range(5):
                for y in range(5):
                    if new_180_arr[x][y] > 0:
                        result_arr, result_cnt = bfs(x, y, new_180_arr, new_180_arr[x][y])
                        #조각이 3개 이상 연결된 경우, 유물이 되고 사라짐 
                        if result_cnt >= 3:
                            new_180_arr = result_arr
                            cnt += result_cnt 

            #만약 유물 가치 합이 현재 최댓값보다 크면 임시 배열에 현재 회전한 배열 저장 
            if cnt > total_max_cnt:
                temp_arr = new_180_arr
                total_max_cnt = cnt

    for i in range(1, 4):
        for j in range(1, 4):
            cnt = 0
            new_270_arr = spin_270(i, j, arr)
            for x in range(5):
                for y in range(5):
                    if new_270_arr[x][y] > 0:
                        result_arr, result_cnt = bfs(x, y, new_270_arr, new_270_arr[x][y])
                        #조각이 3개 이상 연결된 경우, 유물이 되고 사라짐 
                        if result_cnt >= 3:
                            new_270_arr = result_arr
                            cnt += result_cnt 
            #만약 유물 가치 합이 현재 최댓값보다 크면 임시 배열에 현재 회전한 배열 저장 
            if cnt > total_max_cnt:
               temp_arr = new_270_arr
               total_max_cnt = cnt
    

    #최종 가치 합이 0보다 큰 경우 
    if total_max_cnt > 0:
        #회전된 배열로 현재 배열 갱신 
        arr = temp_arr
        #탐사 끝
        #유물이 비어있는 칸 새 유물로 채워주기 : j가 작은 순, i가 큰 순
        #연쇄 유물 획득 
        while True: 
            for j in range(5):
                for i in range(4, -1, -1):
                    if arr[i][j] == 0:
                        if wall:
                            num = wall.popleft()
                            arr[i][j] = num

            add_cnt = 0
            for x in range(5):
                for y in range(5):
                    if arr[x][y] > 0:
                        result_arr, result_cnt = bfs(x, y, arr, arr[x][y])
                        #조각이 3개 이상 연결된 경우, 유물이 되고 사라짐 
                        if result_cnt >= 3:
                            arr = result_arr
                            add_cnt += result_cnt 
                            
            #추가적으로 획득한 유물 가치 확인 
            if add_cnt == 0:
                break
            else:
                total_max_cnt += add_cnt

            total_cnt.append(total_max_cnt)
    else: 
        break





print(' '.join(map(str, total_cnt)))    
            
