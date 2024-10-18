def solution(brown, yellow):
    answer = []
    ylst = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            ylst.append(i)

    for i in range(len(ylst)):
        if ylst[i] * ylst[len(ylst) - i - 1] == yellow:
            r = max(ylst[i], ylst[len(ylst) - i - 1])
            c = min(ylst[i], ylst[len(ylst) - i - 1])
            if (r + 2) * (c + 2) == brown + yellow:
                return r + 2, c + 2

