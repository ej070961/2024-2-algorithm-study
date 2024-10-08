import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    cnt = 0
    
    while queue:
        top = max(queue)
        pop = queue.popleft()
        m -= 1

        if top == pop:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(pop)
            if m < 0:
                m = len(queue) - 1
''' 아래는 람다와 enumerate 사용 풀이
enumerate 로 idx 사용하기 
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(enumerate(map(int, input().split())))  # (index, value) 형태로 저장
    cnt = 0
    
    while queue:
        top = max(queue, key=lambda x: x[1])[1]  # 현재 큐에서 가장 큰 중요도를 찾음
        idx, pop = queue.popleft()  # 큐에서 첫 번째 문서를 꺼냄

        if pop == top:  # 꺼낸 문서가 가장 중요하다면
            cnt += 1
            if idx == m:  # 그 문서가 우리가 궁금한 문서라면
                print(cnt)
                break
        else:
            queue.append((idx, pop))  # 중요하지 않으면 다시 뒤로 보냄
            '''