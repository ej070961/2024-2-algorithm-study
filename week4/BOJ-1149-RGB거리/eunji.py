import sys

input = sys.stdin.readline

#집의 수 N 입력
N = int(input())

price =[[]]*(N+1)

for i in range(1, N+1):
    price[i] = list(map(int, input().split()))

for i in range (2, N+1):
    #R로 칠할 때 최소
    price[i][0] += min(price[i-1][1],price[i-1][2])
    #G로 칠할 때 최소
    price[i][1] += min(price[i-1][0], price[i-1][2])
    #B로 칠할 때 최소
    price[i][2] += min(price[i-1][0], price[i-1][1])


print(min(price[N]))
    