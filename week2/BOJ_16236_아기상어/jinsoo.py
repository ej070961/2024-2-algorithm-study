import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            ci, cj = i,j
            graph[i][j] = 0
    

shark = 2
cnt = ans = 0

def bfs(si,sj):
    # [1] q, v[], 필요 자료형 생성
    q = deque()
    v = [[0] * n for _ in range(n)]
    tlist = []

    # [2] q 에 초기데이터를 삽입, v 표시
    q.append((si,sj))
    v[si][sj] = 1
    eat = 0

    while q:
        ci, cj = q.popleft()
        # 종료 조건 eat == v[ci][cj] # eat에 적힌 거리는 모두 리스트에 넣음
        if v[ci][cj] == eat:
            return tlist,eat - 1
        # 4방향, 범위내, 미방문, 조건 (s나보다 같거나 작은 물고기면)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 상하좌우
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj] ==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
                # 나보다 작은 물고기인 경우 tlist 에 추가
                if shark > graph[ni][nj] > 0:
                    tlist.append((ni,nj)) # 먹을 물고기 append
                    eat = v[ni][nj]
# 방문을 모두 끝낸 경우 -> 먹을 물고기 못참음
    return tlist, eat - 1


while True:
    tlist, dist = bfs(ci,cj)
    if len(tlist) == 0:
        break
    tlist.sort(key = lambda x: (x[0],x[1])) # 행 먼저 열 나중
    ci, cj = tlist[0]
    graph[ci][cj] = 0 # 물고기 먹기
    cnt += 1 # 먹은 갯수
    ans += dist # 거리 누적
    if shark == cnt: # 크기만큼 물고기 먹은 경우 크기 + 1
        shark += 1
        cnt = 0

print(ans)