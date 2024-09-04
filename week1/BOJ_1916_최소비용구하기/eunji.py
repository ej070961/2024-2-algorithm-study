import sys
import heapq



def dijkstra(start):

    q  = []
    #시작점 비용은 0
    heapq.heappush(q, (0, start)) 
    total_cost[start] = 0 #시작점 비용 초기화 

    while q:
        #큐에서 비용이 가장 적은 비용과 도시를 꺼냄 
        current_cost, current_city = heapq.heappop(q)
        #현재 저장된 비용보다 큐에서 나온 비용이 더 크면 무시 
        if total_cost[current_city] < current_cost:
            continue

        #현재 도시에서 갈 수 있는 도시들 탐색 시작
        for next_city, next_cost in bus_info[current_city]:
            new_cost = current_cost + next_cost
            
            #더 적은 비용으로 갈 수 있다면 업데이트
            if total_cost[next_city] > new_cost:
                total_cost[next_city] = new_cost
                heapq.heappush(q, (new_cost, next_city))



INF  = float('inf')
#도시의 개수 
N = int(sys.stdin.readline())
#버스의 개수 
M = int(sys.stdin.readline())

bus_info = [[] for _ in range(N+1)]

total_cost = [INF]*(N+1)
#버스 정보 세팅
for _ in range(M):
    #출발도시, 도착도시, 비용
    x, y, c = map(int,sys.stdin.readline().split(' '))
    #출발도시를 인덱스로 하여 튜플 (도착도시, 비용) 값 추가 
    bus_info[x].append((y, c))


#출발도시, 도착도시 입력
A, B = map(int, sys.stdin.readline().split(' '))

dijkstra(A)
print(total_cost[B])