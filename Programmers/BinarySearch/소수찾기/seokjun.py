from itertools import permutations

def solution(numbers):
    candidate_number_set = set()
    candidate_string_list = list(numbers)
    
    # 모든 자리수에 대한 순열 구하기
    for i in range(1, len(numbers) + 1):
        # permutations 함수를 사용하여 순열을 구함
        for perm in permutations(candidate_string_list, i):
            num = int(''.join(perm))  # 순열을 숫자로 변환
            candidate_number_set.add(num)  # Set에 추가 (중복 제거)
    
    ans = 0
    
    # 소수 개수 확인
    for val in candidate_number_set:
        if is_prime(val):
            ans += 1
    
    return ans

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # n의 제곱근까지만 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

"""
def solution(numbers):
    candidate_number_set = set()
    candidate_string_list = list(numbers)
    res = []
    
    # 순열을 직접 구현하는 함수
    def permutations(arr, n):
        if n == 0:
            return [[]]
        result = []
        for i in range(len(arr)):
            fixed = arr[i]
            rest = arr[:i] + arr[i+1:]  # 현재 요소를 제외한 나머지 배열
            for perm in permutations(rest, n - 1):
                result.append([fixed] + perm)
        return result
    
    # 모든 자리수에 대한 순열 구하기
    for i in range(1, len(numbers) + 1):
        res.extend(permutations(candidate_string_list, i))
    
    # 숫자로 변환
    ret = [int(''.join(p)) for p in res]
    
    # Set을 사용하여 중복 제거
    for num in ret:
        candidate_number_set.add(num)
    
    ans = 0
    
    # 소수 개수 확인
    for val in candidate_number_set:
        if is_prime(val):
            ans += 1
    
    return ans

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # n의 제곱근까지만 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True
"""
