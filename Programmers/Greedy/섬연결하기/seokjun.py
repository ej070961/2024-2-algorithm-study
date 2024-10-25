import sys

def solution(n, costs):
    adjList = [[sys.maxsize] * n for _ in range(n)]
    linkedNodes = set([0])
    answer = 0

    for startNode, endNode, cost in costs:
        adjList[startNode][endNode] = adjList[endNode][startNode] = cost

    while len(linkedNodes) < n:
        minCost = sys.maxsize
        minEndNode = -1
        for startNode in linkedNodes:
            for endNode, cost in enumerate(adjList[startNode]):
                if not endNode in linkedNodes and cost < minCost:
                    minCost = cost
                    minEndNode = endNode
        
        linkedNodes.add(minEndNode)
        answer += minCost
    
    return answer

# print(solution(4, [[0, 1, 1],[0, 2, 2],[1, 2, 5],[1, 3, 1],[2, 3, 8]]))