def solution(answers):
    #첫번째 학생 1부터 5까지 1씩 증가하면서 반복
    #두번재 학생 홀수 문제면 - 답 2 짝수분제면 1부터 1, 3, 4, 5 반복 
    #세번째 학생 3, 1, 2, 4, 5 대로 2번씩 반복 
    member_1 = [1, 2, 3, 4, 5]
    member_2 = [1, 3, 4, 5]
    member_3 = [3, 1, 2, 4, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3= 0
    for index, ans in enumerate(answers):
        member_1_ans = member_1[(index+1) % 5 - 1]
        
        #두번째 학생의 답 계산
        #3번째 학생의 답
        if (index+1) % 2 == 0:
            #짝수번호 문제
            member_2_ans = member_2[ ((index+1) // 2) % 4 - 1]
            member_3_ans =  member_3[ ((index+1) // 2) % 5 - 1]
        else:
            member_2_ans = 2
            member_3_ans = member_3[ ((index+1) // 2 + 1) % 5 - 1]

        print(ans, member_1_ans, member_2_ans, member_3_ans)
        
        if ans==member_1_ans:
            cnt1 += 1
        if ans==member_2_ans:
            cnt2 += 1
        if ans==member_3_ans:
            cnt3+= 1

    answer = []
    max_cnt = max(cnt1, cnt2, cnt3)
    if cnt1 == max_cnt:
        answer.append(1)
    if cnt2 == max_cnt:
        answer.append(2)
    if cnt3 == max_cnt:
        answer.append(3)

    return answer


print(solution([1,3,2,4,2]))