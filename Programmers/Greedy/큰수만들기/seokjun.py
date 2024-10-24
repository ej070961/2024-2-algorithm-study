def solution(number, k):
    stack = []
    count = 0  # 제거된 숫자 카운트
    
    for current in number:
        # 스택이 비어있지 않고, 제거할 기회가 남아있으며, 현재 숫자가 스택 마지막 숫자보다 크면
        while stack and count < k and stack[-1] < current:
            stack.pop()  # 스택에서 제거
            count += 1  # 제거된 숫자 카운트 증가
        
        stack.append(current)  # 현재 숫자를 스택에 추가

    # 만약 제거되지 않은 숫자가 있다면, 남은 숫자를 제거
    # 예: k개의 숫자를 다 제거하지 못한 경우 뒤에서부터 자름
    while count < k:
        stack.pop()
        count += 1

    return ''.join(stack)  # 스택을 문자열로 변환하여 반환

"""
# 시간 초과 난 코드
def solution(number, k):
    delete_count = 0
    answer = ""
    
    while delete_count < k:
        max_digit = -1
        delete_idx = -1
        
        # 가장 큰 숫자를 찾음
        for i in range(k - delete_count + 1):
            cur_digit = int(number[i])
            if cur_digit > max_digit:
                max_digit = cur_digit
                delete_idx = i
        
        # 가장 큰 숫자를 정답에 추가하고, 그 인덱스까지의 문자를 삭제
        answer += number[delete_idx]
        delete_count += delete_idx
        number = number[delete_idx + 1:]
    
    # 남은 숫자를 결과에 추가
    answer += number
    
    return answer
"""