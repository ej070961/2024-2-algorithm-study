# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
def solution(n, lost, reserve):


    #도난 당한 학생이 여벌 옷을 가지고 있는 경우 처리 
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    #여벌 옷을 가진 학생의 번호 
    for i in reserve_set:
        for k in [i-1, i+1]:
            #체육복을 빌려줌
            if k in lost_set:
                lost_set.remove(k)
                break

    
    return n - len(lost_set)

print(solution(5, [1, 4], [1, 3, 5]))