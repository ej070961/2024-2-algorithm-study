def solution(sizes):
    width = 0
    height = 0
    
    # 길이가 긴 가로(세로) 중 가장 긴 것 & 길이가 짧은 가로(세로) 중 가장 긴 것
    for w, h in sizes:
        width = max(max(w, h), width)
        height = max(min(w, h), height)
    
    return width * height