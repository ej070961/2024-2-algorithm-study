def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans_first = []
    ans_second = []
    ans_third = []
    answer = []

    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            ans_first.append(answers[i])
        if answers[i] == second[i % 8]:
            ans_second.append(answers[i])
        if answers[i] == third[i % 10]:
            ans_third.append(answers[i])

    if max(len(ans_first), len(ans_second), len(ans_third)) == len(ans_first):
        answer.append(1)
    if max(len(ans_first), len(ans_second), len(ans_third)) == len(ans_second):
        answer.append(2)
    if max(len(ans_first), len(ans_second), len(ans_third)) == len(ans_third):
        answer.append(3)

    return answer

