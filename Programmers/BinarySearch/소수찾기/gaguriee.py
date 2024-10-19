import itertools

def solution(numbers):
    
    primes = set()  # 중복을 방지하기 위해 set 사용
    for r in range(1, len(numbers) + 1):
        permutations = itertools.permutations(numbers, r)
        
        for perm in permutations:
            # 순열을 숫자로 변환 (앞에 0이 있는 경우는 제외하지 않음)
            num = int(''.join(map(str, perm)))
            if is_prime(num):
                primes.add(num)
    
    return len(primes)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False 
    return True