import sys
from collections import deque 
input = sys.stdin.readline

#테스트 케이스 개수 입력
case_num = int(input())

for case in range(case_num):
    #N: 문서의 개수
    #M: 몇번째로 인쇄되었는지 궁금한 문서가 현재 Queue에 놓여있는 인덱스
    N, M = map(int, input().split())

    q = deque()
    
    # 중요도와 문서의 인덱스를 deque에 추가 
    for index, data in enumerate(list(map(int, input().split()))):
        q.append((data, index))


    cnt = 0

    while q:
        #가장 높은 중요도 갱신 
        max_num = max(q)
        #현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인
        item = q.popleft()
        
        #중요도가 가장 높은 문서라면 
        if item[0] == max_num[0]:
            #프린트
            cnt += 1
       
            #찾고자하는 문서의 인덱스와 같다면, 결과 출력
            if item[1] == M:
                print(cnt)
                break
        else:
            #중요도가 가장 높은 문서가 또 있다면, 가장 뒤에 재배치 
            q.append(item)