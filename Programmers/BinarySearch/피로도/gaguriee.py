import itertools

def solution(k, dungeons):
    answer = -1
    permutations = itertools.permutations(dungeons)
    
    for perm in permutations:
        
        total = k
        cnt = 0
        
        for i in range(len(perm)):
            if total >= perm[i][0]:
                total = total - perm[i][1]
                cnt = cnt + 1
        
        answer = max(answer, cnt)
    
    
    return answer
