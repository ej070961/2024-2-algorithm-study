#문제설명
#Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 카펫: 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫
def solution(brown, yellow):
    # 카펫의 크기 = 격자 수의 합 
    size = brown + yellow
    brown - 4

    #너비의 길이는 yellow 격자수 + 브라운 격자 수 2개 
    for w in range(3, yellow+3):
        # 넓이가 너비로 나눠진다면
        if size % w == 0:
            #높이 설정
            h = size // w
            #(높이-2) x (너비-2) = yellow 카펫의 넓이
            if (h-2)*(w-2) == yellow:
                #가로가 세로보다 길거나 같기 때문에 이렇게 세팅
                answer = [max(w, h), min(w,h)]
    
                return answer

print(solution(24,24))