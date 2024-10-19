import sys

input = sys.stdin.readline

#숲의 크기 R, C, 정령의 수 K
R, C, K = map(int, input().split())
#각 골렘의 출발 열 ci, 출구 방향 정보 di를 저잗할 배열 
unit = []

#방향 정보: 북 동 남 서 
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for _ in range(K):
    c, d = map(int, input().split())
    unit.append((c, d))

# 탐색할 숲 배열 초기화
arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
exit_set = set()
ans = 0
num = 2


def bfs (i, j):
    q = []
    visited = [[0]*(C+2) for _ in range(R+4)]
    max_i = 0 #-2해서 리턴 
    q.append((i, j))
    visited[i][j] = 1

    while q:
        r, c = q.pop(0)
        max_i = max(max_i, r)

        #네방향, 미방문, 같은값 또는 내가 출구 - 상대방이
        for di, dj in ((-1,0), (1, 0), (0,-1), (0, 1)):
            ni = r + di
            nj = c + dj

            if visited[ni][nj] == 0  and (arr[ni][nj] == arr[r][c] or ((r, c) in exit_set and arr[ni][nj]>1)):
                q.append((ni, nj))
                visited[ni][nj] = 1

    return max_i - 2

#정령 순서 대로 탐색 
for c, d in unit:
    r = 1 # 시작 행은 1
    #[1]남쪽으로 최대한 이동 (남쪽 -> 서쪽 -> 동쪽)
    while True:
        #남쪽 이동 가능 여부 체크
        if (arr[r+1][c-1] + arr[r+1][c+1] + arr[r+2][c]) == 0:
            r += 1
        #서쪽으로 회전하면서 아래로 한칸 
        elif (arr[r-1][c-1]+ arr[r][c-2] + arr[r+1][c-1] + arr[r+1][c-2] + arr[r+2][c-1])== 0:
            r += 1
            c -= 1
            d = (d-1) % 4
        #동쪽으로 회전하면서 아래로 한칸 
        elif (arr[r-1][c+1]+ arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c+1] + arr[r+1][c+2]) == 0:
            r += 1
            c += 1 
            d = (d+1) % 4
        else:
            break
    
    #[2] 골렘을 표시
    if r < 4: #골렘의 몸이 범위 밖에 있음 
        arr = [[1]+[0]*C+[1] for _ in range(R+3)] + [[1]*(C+2)]
        exit_set = set()
        num = 2
    else: #나를 표시 + 골렘의 출구 위치 추가 
        arr[r-1][c] = arr[r+1][c] = arr[r][c-1] = arr[r][c] = arr[r][c+1] = num
        num += 1 
        exit_set.add((r+di[d], c+dj[d]))
        ans += bfs(r, c)
    
print(ans)