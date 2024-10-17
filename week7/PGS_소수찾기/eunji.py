#문제 설명
#각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

from itertools import permutations

def is_prime_number(number):
    
    if number==1:
        return False
    if number==2:
        return True
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def solution(numbers):
    number_set = []
    for i in range(len(numbers)):
        number_set.append(numbers[i])
    answer = 0
    prime_set = []
    for i in range(1, len(numbers)+1):
        #순열 라이브러리를 통한 해당 자릿수의 모든 조합의 수 구하기 
        check_num = list(map(''.join, permutations(number_set, i)))
        for i in check_num:
            #조합된 숫자의 첫자리가 0일 경우 예외처리 
            if i[0] == '0':
                continue
            #조합된 숫자가 현재 소수 배열에 포함되는지 여부 확인 
            if i not in prime_set:
                if(is_prime_number(int(i))):
                    answer += 1
                    prime_set.append(i)
    
  
    return answer

print(solution("011"))