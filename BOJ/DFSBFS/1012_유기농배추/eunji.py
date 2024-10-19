import sys
sys.setrecursionlimit(100000)

def dfs(graph, dy, dx):
    #방문했다고 체크
    graph[dy][dx] = -1
  
    for y, x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        #범위 체크
        if 0 <=  dy+y <= N-1 and 0 <= dx+x <= M-1: 
            #인접해 있는 노드를 확인했을 때, 배추가 심어져 있다면, 
            if graph[dy+y][dx+x] == 1:
                dfs(graph, dy+y, dx+x)
    
    return


#테스트 케이스 개수
T = int(sys.stdin.readline())

#답을 저장할 변수
answer = []

for _ in range(T):
    #가로길이, 세로길이, 위치 개수
    M, N, K = map(int, sys.stdin.readline().split(' '))

    #배추밭 그래프
    land = [[0 for _ in range(M)] for _ in range(N)]

    
    ans = 0

    for _ in range(K):
        X,Y = map(int, sys.stdin.readline().split(' '))
        #배추가 심어져 있는 위치 표시 
        land[Y][X] = 1
    
    #탐색 시작
    for dy in range(N):
        for dx in range(M):
            #배추가 심어져있다면, 
            if land[dy][dx] == 1:
                # 답 1증가
                ans += 1
                dfs(land, dy, dx)


    answer.append(ans)
    # print(T, M, N, K)
    # print(land)

for i in answer:
    print(i)

