import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]  
arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]

# 출구 위치 set 저장
exit_set = set()

# 시계방향, 상 우 하 좌 
di =  [-1, 0, 1, 0]
dj =  [ 0, 1, 0,-1]

ans = 0

# 골렘 위치 표시할 num (2부터 시작)
num = 2

# 골룸 내리기 끝난 뒤 가장 남쪽 index (max_i) 찾기
# * 최종 index에 -2 하기
def bfs(si,sj): # si, sj는 정령의 위치 (중앙)
    q = []
    q.append((si,sj))

    # 배열에 대해 방문 여부 새로 초기화
    visited = [[0]*(C+2) for _ in range(R+4)]
    visited[si][sj]=1 

    max_i = 0 

    while q:
        ci,cj = q.pop(0)
        max_i = max(max_i, ci)

        # 네방향, 미방문, 조건: 같은값 또는 내가 출구 - 상대방이 골렘
        for i in range(4):
            ni,nj = ci+di[i], cj+dj[i]

            # 미방문 & 골렘 내부(같은 값) & 현재 출구이면서 골렘과 닿아있을 때
            if visited[ni][nj]==0 and (arr[ci][cj]==arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj]>1)):
                q.append((ni,nj))
                visited[ni][nj]=1

    return max_i-2

for cj,dr in unit:

    ci=1 # 시작 i는 무조건 1

    # 골렘 남쪽으로 최대한 이동하기
    while True:
        # 남쪽 이동 가능
        if arr[ci+1][cj-1]+arr[ci+2][cj]+arr[ci+1][cj+1]==0:
            ci+=1
        # 서쪽 방향으로 회전하면서 내려감
        elif (arr[ci-1][cj-1]+arr[ci][cj-2]+arr[ci+1][cj-1]+arr[ci+1][cj-2]+arr[ci+2][cj-1])==0:
            ci+=1
            cj-=1
            dr=(dr-1)%4
        # 동쪽 방향으로 회전하면서 내려감
        elif (arr[ci-1][cj+1]+arr[ci][cj+2]+arr[ci+1][cj+1]+arr[ci+1][cj+2]+arr[ci+2][cj+1])==0:
            ci+=1
            cj+=1
            dr=(dr+1)%4
        else:
            break

    # 골렘 몸이 범위 밖일 경우 
    # 정령의 위치 ci는 골렘의 중앙, ci-1이 0,1,2 중 있으면 안됨 (ci-1<3)
    if ci<4:
        arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
        exit_set = set()
        num = 2
    else:
        # 골렘 표시
        arr[ci+1][cj]=arr[ci-1][cj]=num
        arr[ci][cj-1:cj+2]=[num]*3
        num+=1

        # 출구 위치 추가
        exit_set.add((ci+di[dr], cj+dj[dr]))

        # 정령이 갈 수 있는 가장 남쪽의 위치 찾기
        ans+=bfs(ci,cj)

print(ans)