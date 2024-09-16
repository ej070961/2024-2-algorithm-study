import sys

input = sys.stdin.readline


def dfs(i, j):

    stack = [(i, j)]
    #방문했다고 표시 
    graph[i][j] = -1

    #넓이 체크할 변수
    cnt = 1

    while stack:
        cur = stack.pop()

        #연결된 곳 체크 
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = cur[0] + dx
            y = cur[1] + dy

            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] == 1:
                    #방문했다고 표시
                    graph[x][y] = -1
                    #넓이 1증가
                    cnt += 1
                    stack.append((x, y))
    return cnt

 
#세로, 가로 입력
n, m = map(int, input().split())

#그래프 초기화
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

#그림의 넓이를 담을 리스트
ans = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans.append(dfs(i, j))


print(len(ans))
print( max(ans) if len(ans)> 0 else 0)







