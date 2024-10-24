import itertools

def solution(word):
    
    dictionary = ['A', 'E', 'I', 'O', 'U']

    dict_list = []
    for i in range(1, 6):
        dict_list.extend(list(map(''.join, itertools.product(dictionary, repeat= i))))

    dict_list.sort()

    for i, w in enumerate(dict_list):
        if w == word:
            return i+1
    

print(solution("AAAAE"))