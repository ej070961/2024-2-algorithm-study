def solution(word):
    result = 0
    
    chars = ['A', 'E', 'I', 'O', 'U']
    
    # 자릿수별 가능한 단어 수
    # 첫번째 자리가 E (index 2)로 시작하면, A (index 1)로 시작하는 모든 단어 건너띔 
    # (5^4 + 5^3 + 5^2 + 5^1 + 5^0  =  625 + 125 + 25 + 5 + 1 = 781)
    weights = [781, 156, 31, 6, 1]
    
    for i, char in enumerate(word):
        index = chars.index(char)
        result = result + weights[i] * index + 1

    return result
