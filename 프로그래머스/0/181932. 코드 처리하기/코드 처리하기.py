def solution(code):
    mode = 0
    ret = ""
    
    for idx, ch in enumerate(code):
        if ch == "1":
            mode = 1 - mode  
            continue
        
        if mode == 0 and idx % 2 == 0:
            ret += ch
        elif mode == 1 and idx % 2 == 1:
            ret += ch
    
    return ret if ret else "EMPTY"
