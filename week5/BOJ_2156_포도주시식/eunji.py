import sys

input = sys.stdin.readline

#포도주 잔의 개수 입력
n = int(input())

#i번째 포도주의 양 
arr = []

#포도주 배열 세팅
for _ in range(n):
    arr.append(int(input()))

#dp[i] = i번째 포도주에서 마신 포도주의 최댓값 
dp = [0]*n

#첫번재 포도주 = 마시는게 최대
dp[0] = arr[0]

if n >= 2:
    #두번째 포도주 = 1번째 포도주 마시고, 2번째도 마시는게 최대 
    dp[1] = arr[0] + arr[1]
    if n >= 3: 
        # 3번째 포도주
        # 마시지 않음
        # 첫번째 마시고, 3번째 마시기
        # 두번째 마시고, 3번째 마시기 
        dp[2] = max(max(arr[0], arr[1]) + arr[2], dp[1])
        for i in range(3, n):
            # 3가지 경우의 값 고려 
            # 현재 잔을 마시지 않는 경우 
            # 이전이전 잔을 마시고, 현재 잔을 마시는 경우
            # 이전이전이전 잔을 마시고, 이전 잔을 마시고 현재 잔을 마시는 경우 값 비교 
            dp[i] = max(max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i], dp[i-1])

#dp[n-1]출력: 마지막 포도주까지 왔을 때 마신 최대 포도주 양 
print(dp[n-1])

