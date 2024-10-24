def solution(routes):
    # 차량 경로가 끝나는 지점을 기준으로 정렬
    routes.sort(key=lambda route: route[1])
    
    count = 0
    cameraPos = -30001
    
    for route in routes:
        # 현재 차량의 시작 지점이 마지막 카메라 위치 이후인 경우, 현재 차량의 끝나는 지점에 카메라를 설치
        if cameraPos < route[0]:
            count += 1
            cameraPos = route[1]
    
    return count
    
    