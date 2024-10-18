# 최소 필요 피로도: 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# 소모 피로도: 던전을 탐험한 후 소모되는 피로도
# 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 
# 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성

visited = []
answer = 0
#피로도, 던전 방문 수, 던전 배열
def dfs(k, cnt, arr):
    global answer
    #방문 수가 현재 최대 방문 수보다 크다면 answer 값 갱신 
    if cnt > answer:
        answer = cnt 
    for j in range(len(arr)):
        if k >= arr[j][0] and not visited[j]:
            visited[j] = True #방문 표시 
            dfs(k - arr[j][1], cnt + 1, arr) #다음 던전을 탐색 
            visited[j] = False #백트래킹: 재귀적 호출이 끝나면 방문하지 않은 상태로 되돌림 다른 경우의 수를 탐색하기 위해 

def solution(k, dungeons):
    global visited
    #dfs를 위한 방문 배열 생성 
    visited = [False] * len(dungeons)

    #모든 던전에 대해 탐색 시작 
    dfs(k, 0, dungeons)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]] ))