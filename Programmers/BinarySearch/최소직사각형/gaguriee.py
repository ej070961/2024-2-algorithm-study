def solution(sizes):
    
    # w,h를 w가 항상 더 크거나 같게 조정
    # w의 max값, w의 max값 구하기
    
    max_w = 0
    max_h = 0
    
    for size in sizes:
        
        w = size[0]
        h = size[1]
        
        if w < h :
            # w가 h보다 작으면 가로로 눕히기
            tmp = w
            w = h
            h = tmp
            
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        
    return max_w * max_h
