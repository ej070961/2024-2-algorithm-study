def solution(n, lost, reserve):
    students = [1] * n
    
    for studentNumber in lost:
        students[studentNumber - 1] -= 1
    
    for studentNumber in reserve:
        students[studentNumber - 1] += 1
        
    for idx in range(len(students)):
        # 여벌 체육복 없는 학생은 패스
        if students[idx] <= 1:
            continue
        
        # 여벌 체육복 있는 학생은 앞뒤 학생 체육복 상태 보고 빌려줄지 말지 결정
        if idx - 1 >= 0:
            if students[idx - 1] < 1: 
                students[idx - 1] += 1
                students[idx] -= 1
                continue
        if idx + 1 < n:
            if students[idx + 1] < 1: 
                students[idx + 1] += 1
                students[idx] -= 1
            
    
    return len(list(filter(lambda val: val > 0, students)))