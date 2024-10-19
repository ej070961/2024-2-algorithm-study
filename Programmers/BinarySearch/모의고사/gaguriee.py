def solution(answers):
    
    method_1 = [1,2,3,4,5]
    method_2 = [2,1,2,3,2,4,2,5]
    method_3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer = []
    
    score_1, score_2, score_3 = 0, 0, 0
    
    for i in range(len(answers)):
        if method_1[i % len(method_1)] == answers[i]:
            score_1 += score_1
        if method_2[i % len(method_2)] == answers[i]:
            score_2 += score_2
        if method_3[i % len(method_3)] == answers[i]:
            score_3 += score_3
    
    if score_1 >= score_2 and score_1 >= score_3:
        answer.append(1)
    if score_2 >= score_1 and score_2 >= score_3:
        answer.append(2)
    if score_3 >= score_1 and score_3 >= score_2:
        answer.append(3)    
        
    return answer

print(solution([1,2,3,4,5]))