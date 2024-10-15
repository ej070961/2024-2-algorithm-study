def solution(answers):
    way1 = [1,2,3,4,5]
    way2 = [2,1,2,3,2,4,2,5]
    way3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = cnt2 = cnt3 = 0
    
    for i in range(len(answers)):
        answer = answers[i]
        if answer == way1[i%5]: cnt1 += 1
        if answer == way2[i%8]: cnt2 += 1
        if answer == way3[i%10]: cnt3 += 1
    
    maxScore = max(cnt1, cnt2, cnt3)
    
    res = []
    
    if cnt1 == maxScore:
        res.append(1)
    if cnt2 == maxScore:
        res.append(2)
    if cnt3 == maxScore:
        res.append(3)

    return res