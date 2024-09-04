import sys
import heapq

N = int(input()) # 도시
M = int(input()) # 버스 
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b ,cost = map(int, input().split())
    graph[a].append((b, cost))

# 출발, 도착
start, end = map(int, input().split())

# 각 도시까지 최소 비용 리스트, 초기값은 무한대
distance = [float('inf')] * (N+1)

def dijkstra(start):
    distance[start] = 0 
    heap = [(0, start)] # (비용, 도시)

    while heap:
        dist, now = heapq.heappop(heap) # 가장 비용 낮은 도시 꺼내기
        if distance[now] < dist: # 중복 방지
            continue

        for next_node, next_cost in graph[now]:
            cost = dist + next_cost 
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

dijkstra(start)
print(distance[end])
