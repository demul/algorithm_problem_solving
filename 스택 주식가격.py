import collections

MAX_PRICE=10000

def solution(prices):
##############스택 구현##########################
    answer = [0 for i in range(len(prices))]
    DQ = collections.deque()
    idx_val_time = [[i, v] for i, v in enumerate(prices)]
    time = 0
    
    for i in idx_val_time :
        while(not(not(DQ))):
            if(DQ[0][1]>i[1]):
                tmpidx = DQ.popleft()[0]
                answer[tmpidx] = time - tmpidx
            else:
                break
        time += 1    
        DQ.appendleft(i)
        
    while(not(not(DQ))):
        tmpidx = DQ.popleft()[0]
        answer[tmpidx] = time - tmpidx - 1
        
    return answer
    
##############브루트 포스 구현#################    
# def solution(prices):
#     time_val = []
#     for i in prices :
#         for j in time_val :
#             if(j[2]==-1) :
#                 continue
            
#             j[0] += 1
#             if(j[1]>i) :
#                 j[2] = -1
        
#         time_val.append([0, i, 1])
    
    
#     answer = [i[0] for i in time_val]
#     return answer
