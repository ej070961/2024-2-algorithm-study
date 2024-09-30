# BOJ-14267-회사_문화_1
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

worker = [0] + list(map(int,input().split()))

compliment = [0] * len(worker)

for _ in range(m):
    i, w = map(int,input().split())
    compliment[i] += w

for i in range(2,n+1):
    compliment[i] += compliment[worker[i]]

answer = []

for i in compliment[1:]:
    answer.append(str(i))

print(' '.join(answer))