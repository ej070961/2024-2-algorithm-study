import heapq
import sys

INF = float('inf')
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M) :
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

x, y = map(int, input().split())

ans = [INF for _ in range(N+1)]

def dijkstra(start) :
    ans[start] = 0
    heap = []
    heap.append([start, 0]) # start부터 start까지의 거리는 0

    while heap :
      start, cost = heapq.heappop(heap)
      if ans[start] < cost :
        continue
      
      for idx, value in enumerate(graph[start]) :
        next_cost = cost + value
        if ans[idx] > next_cost : # 갱신할 비용이 minimum일 경우
            ans[idx] = next_cost
            heapq.heappush(heap, [idx, next_cost])
  
dijkstra(x) 
     
print(ans[y])
