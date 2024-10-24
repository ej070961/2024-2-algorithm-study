def solution(k, dungeons):
    global answer
    answer = 0
    
    def bt(curFatigue, visitCount, visited):
        global answer
        if visitCount > answer:
            answer = visitCount
        
        for i in range(len(dungeons)):
            minFatigue, consumeFatigue = dungeons[i]
            
            if not visited[i] and curFatigue >= minFatigue:
                visited[i] = True
                bt(curFatigue - consumeFatigue, visitCount + 1, visited)
                visited[i] = False
    
    bt(k, 0, [False] * len(dungeons))
    return answer