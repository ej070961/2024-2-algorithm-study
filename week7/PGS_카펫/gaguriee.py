def solution(brown, yellow):
    answer = []
    
    # 노란색 카펫 = w, h
    # 갈색 카펫 개수 = (w+2)*2 + h*2 = 2w + 2h + 4
    
    comb = []
    
    total = brown + yellow
    
    for i in range(3, total+1, 1):
        # w * h = total의 w, h 구하기
        if total % i == 0 : 
            w = i - 2
            h = total//i - 2
            
            # 가로길이가 세로길이보다 작을 경우
            if w < h :
                tmp = w
                w = h
                h = tmp
            
            # w, h 조합 중에 2w + 2h + 4 = brown인 경우 전달
            if 2*w + 2*h + 4 == brown:
                answer.append(w+2)
                answer.append(h+2)
                return answer
