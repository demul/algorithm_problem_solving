import collections
import math
def solution(progresses, speeds):
    answer = []
    
    Q_p = collections.deque(progresses)
    Q_s = collections.deque(speeds)
    
    total_day = 0
    
    
    while not(not Q_p):
        how_long_it_takes = math.ceil((100 - Q_p[0] - total_day * Q_s[0]) / Q_s[0])
        total_day += how_long_it_takes
        
        this_cnt = 1
        Q_p.popleft()
        Q_s.popleft()
        
        while(not(not Q_p) and 
              (Q_p[0] + total_day * Q_s[0] >= 100)):
            this_cnt += 1
            Q_p.popleft()
            Q_s.popleft()
            
        answer.append(this_cnt)
        
    
    return answer
