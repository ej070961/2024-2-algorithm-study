import sys

input = sys.stdin.readline
R,C,K = map(int,input().split())
unit = [list(map(int,input().split())) for _ in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
exit_set = set() # 출구
#    상 우 하 좌
di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(si,sj):
    q = []
    v = [[0]*(C+2) for _ in range(R+4)]
    maxi = 0 # -2 해서 리턴
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        maxi = max(maxi, ci)
        # 네방향, 미방문, 조건: 같은값 또는 내가 출구 - 상대방이 골렘
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di, cj+dj
            if v[ni][nj] == 0 and (arr[ci][cj] == arr[ni][nj] or ((ci,cj) in exit_set and arr[ni][nj] > 1)):
                q.append((ni,nj))
                v[ni][nj] = 1
    return maxi - 2


answer = 0
number = 2 #(골렘번호)

for cj, dr in unit:
    ci = 1 
    while True:
        # 수직으로 내려가기
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0:
            ci += 1
        # 왼쪽 회전하며 내려가기 (왜 5칸을 확인하지...?) 나는 3칸이라고 생각하는데 아직도 이해가 안댐 (3칸하면 에러남)
        # 서쪽(왼쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj-1]+arr[ci][cj-2]+arr[ci+1][cj-1]+arr[ci+1][cj-2]+arr[ci+2][cj-1])==0:
            ci+=1
            cj-=1
            dr=(dr-1)%4
        # 동쪽(오른쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj+1]+arr[ci][cj+2]+arr[ci+1][cj+1]+arr[ci+1][cj+2]+arr[ci+2][cj+1])==0:
            ci+=1
            cj+=1
            dr=(dr+1)%4
        else:
            break

    if ci < 4: # 몸이 범위 밖(새롭게 탐색 시작. arr 초기화)
        arr = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
        exit_set = set()
    else:
        # 골렘 표시 + 비상구 위치 추가
        arr[ci+1][cj] = arr[ci-1][cj] = number
        arr[ci][cj-1:cj+2] = [number] * 3
        number += 1

        exit_set.add((ci + di[dr], cj + dj[dr])) # 이게 이해가 안되네

        answer += bfs(ci,cj) 

print(answer)

