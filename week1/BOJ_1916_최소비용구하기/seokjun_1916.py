import heapq

N = int(input())
M = int(input())
adjList = {}

for _ in range(M):
  start, end, cost = map(int, input().split(" "))
  if start not in adjList:
    adjList[start] = []
  adjList[start].append((end, cost))

A, B = map(int, input().split(" "))

def dijkstra(start):
  INF = float('inf')
  distances = [INF] * (N + 1)
  distances[start] = 0

  pq = []
  heapq.heappush(pq, (0, start)) 

  while pq:
    currentDist, current = heapq.heappop(pq)

    if distances[current] < currentDist:
      continue

    if current in adjList:
      for neighbor in adjList[current]:
        nextNode = neighbor[0]
        nextDist = currentDist + neighbor[1]

        if nextDist < distances[nextNode]:
          distances[nextNode] = nextDist
          heapq.heappush(pq, (nextDist, nextNode))

  return distances


distances = dijkstra(A)
print(distances[B])
