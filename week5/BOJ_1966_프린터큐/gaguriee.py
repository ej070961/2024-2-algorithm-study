from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    # 문서의 개수 N, 궁금한 문서의 위치 M 
    N, M = map(int, input().split())
    
    # 문서들의 중요도 
    priorities = list(map(int, input().split()))
    
    queue = deque((i, priorities[i]) for i in range(N))
    print_order = 0

    while True:
        current = queue.popleft()
        
        # 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(current[1] < doc[1] for doc in queue):
            queue.append(current)  # 중요도가 높은 문서가 있으면 다시 뒤로 보냄
        else:
            print_order += 1  # 인쇄된 순서를 증가시킴
            if current[0] == M:  # 우리가 찾는 문서가 인쇄되었는지 확인
                print(print_order)  # 인쇄 순서 출력
                break
