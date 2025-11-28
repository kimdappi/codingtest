from collections import deque
import math

def solution(progresses, speeds):
    prog_q= deque(progresses)
    speed_q= deque(speeds)
    
    result =[]
    
    while prog_q:
        for i in range(len(prog_q)):
            prog_q[i]+=speed_q[i]
        
        okay =0
        while prog_q and prog_q[0]>=100:
            prog_q.popleft()
            speed_q.popleft()
            okay+=1

        if okay>0:
            result.append(okay)
    return result
        