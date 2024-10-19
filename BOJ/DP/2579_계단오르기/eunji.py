import sys

input = sys.stdin.readline

#계단 수 N 입력
N = int(input())

# 각 계단에 대한 점수를 저장할 배열 초기화
stairs = [0] * (N+1)

for i in range(N):
    stairs[i+1] = int(input())

# 각 계단에서 얻을 수 있는 점수 최댓값 담을 dp 테이블 초기화
dp = [0] * (N+1)

# 0 -> 1 1 -> 2/1->3  2 ->3/ 2 -> 4 4->5/4->6
#0 ->2 2 -> 3/2 -> 4

#첫번째 계단의 최댓값은 밟았을 경우
dp[1] = stairs[1]

if N==1:
    print(dp[N])
elif N==2 :
    print(dp[1] + stairs[2])
else:
    #두번째 계단의 최댓값은 1, 2번째 계단을 연속으로 밟을 경우
    dp[2] = dp[1] + stairs[2]
    for i in range(3, N+1):
        #세칸 연속 밟을 수 없음 
        #따라서 각 계단의 최댓값은 i-2 계단을 밟고 현재 계단을 밟을 경우와 i-3, i-1을 밟고 현재 계단을 밟을 경우 비교
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(dp[N])