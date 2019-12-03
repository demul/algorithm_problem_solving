def solution(arrangement):
    answer = 0
    DQ = 0
    ###레이저를 r로 치환
    arrangement = arrangement.replace("()", "r")
    
    ###빼면서 정리
    for i in arrangement :
        if (i == "(") :
            DQ += 1
        elif (i == "r") :
            answer += DQ
        else :
            DQ -= 1
            answer += 1
            
    return answer
