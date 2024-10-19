import sys

input = sys.stdin.readline

#첫번째 수열 입력 
arr1 = input().rstrip()
#2번째 수열 입력
arr2 = input().rstrip()

#DP 테이블 초기화 
#dp[i][j] = 첫번째 수열의 i번째 까지와 두번째 수열의 j번째 까지의 LCS 길이
dp = [[0 for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]
for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        #dp에서 i일때, arr1은 i-1을 뜻함
        #dp에서 j일때, arr2은 j-1을 뜻함
        if arr1[i-1] == arr2[j-1]:
            #값이 같으면, LCS에 추가 
            dp[i][j] = dp[i-1][j-1] + 1
        else: 
            #같지 않을 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(arr1)][len(arr2)])