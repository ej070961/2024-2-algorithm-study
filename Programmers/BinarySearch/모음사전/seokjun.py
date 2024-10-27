def solution(word):
    # 재귀적으로 단어를 생성하는 방식으로 모든 경우를 사전순으로 구한 후, 주어진 단어의 순서를 반환
    # 각 자리가 결정하는 단어의 개수
    weights = [781, 156, 31, 6, 1]  # 5^4, 5^3, 5^2, 5^1, 5^0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    result = 0
    
    # 각 자리의 알파벳이 몇 번째인지 계산하여 결과에 반영
    for i, char in enumerate(word):
        index = vowels.index(char)
        result += index * weights[i] + 1
    
    return result
