def solution(word):
    result = 0
    
    chars = ['A', 'E', 'I', 'O', 'U']
    
    weights = [781, 156, 31, 6, 1]
    
    for i, char in enumerate(word):
        index = chars.index(char)
        result = result + weights[i] * index + 1

    return result
