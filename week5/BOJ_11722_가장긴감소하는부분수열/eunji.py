import sys

input = sys.stdin.readline

#수열의 크기 
N = int(input())

#수열을 이루고 있는 요소 입력 받아 수열 배열 초기화
target = list(map(int, input().split()))

# dp[i] = target[i]가 감소 부분 배열의 마지막 요소일 때, 감소배열의 길이
dp = [1] * N # 각 감소배열 초기값 자기 자신이 포함되므로 1 세팅 

#배열의 1인덱스부터 요소부터 탐색 
for i in range(1, N):
    #target[i]를 기준으로 target[0]부터 target[i-1]를 순환하며 크기 비교 
    for j in range(i):
        #target[i]가 j번째 인덱스 요소보다 작을 경우 
        if target[i] < target[j]:
            # target[i]가 마지막 요소인 감소부분배열의 길이 
            # = max( 현재 저장된 감소부분배열의 길이, dp[j] 감소부분배열에 target[i]를 추가한 배열의 길이)
            dp[i] = max(dp[i],dp[j]+1)

#각 감소부분배열 중 최댓값
print(max(dp))


