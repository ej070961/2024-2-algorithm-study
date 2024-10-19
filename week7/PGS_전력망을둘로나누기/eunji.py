#wires[i] = [v1 송전탑, v2 송전탑]

visited = []
count = []
answer = float('inf')

def dfs (cnt, point, arr):
    global visited
    visited = [False] * len(arr)
    stack = [point]

    while stack:
        x = stack.pop()
        cnt += 1
        for i in range(len(arr)):
            # 방문하지 않았다면
            if not visited[i]:
                #해당 지점에 연결된 송전탑이 있다면 
                if x == arr[i][0]:
                    visited[i] = True
                    stack.append(arr[i][1])
                elif x == arr[i][1]:
                    visited[i] = True
                    stack.append(arr[i][0])

    return cnt



def solution(n, wires):
    global answer
    if n == 2:
        return 0
    
    for i in range(0, n-1):

        v1, v2 = wires[i]
        new_wires = wires[:i] + wires[i+1:]
        
        x = dfs(0, v1, new_wires)
        y = dfs(0, v2, new_wires)

       
        answer = min(answer, abs(x-y))
        

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))