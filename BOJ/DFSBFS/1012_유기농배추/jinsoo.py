import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] # 알려줄 사람 이거 어캐 동작하는지
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            graph[nx][ny] = -1 # visited 
            dfs(nx,ny)

# 입력받기
T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split()) # M = 가로, N = 세로, K = 배추 개수
    graph = [[0] * M for _ in range(N)] # 그래프 0으로 기본 설정
    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1 # 주의 : graph[세로][가로] 로 입력 받아야함 그래야 보이는대로 그려짐
    
    count = 0
    for i in range(N): # 1열부터 가로로 탐색 
        for j in range(M): 
            if graph[i][j] == 1:
                dfs(i,j) # 배추가 있으면 dfs 탐색
                count += 1 # 배추 개수 증가
    print(count)