from collections import deque

def solution(n, wires):
    answer = n
    
    # BFS로 전력망의 크기를 계산하는 함수
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
                    
        return count
    
    for i in range(len(wires)):
        # 그래프 초기화
        graph = [[] for _ in range(n + 1)]
        
        # 전선 중 하나를 끊고 나머지로 그래프를 생성
        for j in range(len(wires)):
            if i != j:
                a, b = wires[j]
                graph[a].append(b)
                graph[b].append(a)
        
        # BFS로 각 전력망의 크기 계산
        visited = [False] * (n + 1)
        tower1_size = bfs(1, graph, visited)
        tower2_size = n - tower1_size
        
        # 두 전력망의 크기 차이를 계산하여 최소값을 업데이트
        diff = abs(tower1_size - tower2_size)
        answer = min(answer, diff)
    
    return answer
