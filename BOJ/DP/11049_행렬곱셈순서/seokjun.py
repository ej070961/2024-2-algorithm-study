import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
R = []
C = []

for i in range(1, N + 1):
    r, c = map(int, data[i].split())
    R.append(r)
    C.append(c)

# greedy: 실패
def solve1(N, R, C):
    res = 0
    while len(R) > 2:
        max_val = 0
        max_idx = 0
        for i in range(1, len(R) - 1):
            if R[i] > max_val:
                max_val = R[i]
                max_idx = i
        res += R[max_idx - 1] * R[max_idx] * C[max_idx]
        C[max_idx - 1] = C[max_idx]
        R.pop(max_idx)
        C.pop(max_idx)
    res += R[0] * R[1] * C[1]
    return res

print(solve1(N, R, C))
