def solution(brown, yellow):
    x = yellow  # 노란색 타일의 가로 길이
    y = yellow / x  # 노란색 타일의 세로 길이
    
    # 가로 길이가 세로 길이보다 크거나 같을 때만 진행
    while x >= y:
        # y가 정수인지 확인
        if y.is_integer():
            # 조건: 갈색 타일의 개수와 일치하는지 확인
            if x + y + 2 == brown / 2:
                return [int(x + 2), int(y + 2)]  # 가로, 세로 길이를 반환
        
        x -= 1  # 가로 길이를 줄임
        y = yellow / x  # 세로 길이를 갱신
