def solution(sizes):
    answer = 0
    max_row = []
    max_column = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            max_row.append(sizes[i][0])
            max_column.append(sizes[i][1])
        else:
            max_row.append(sizes[i][1])
            max_column.append(sizes[i][0])

        answer = max(max_row) * max(max_column)
    return answer
