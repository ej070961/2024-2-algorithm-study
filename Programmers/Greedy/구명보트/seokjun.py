def solution(people, limit):
    people.sort()
    result = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        if people[i] + people[j] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
        result += 1
            
    return result