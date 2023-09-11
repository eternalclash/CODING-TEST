from collections import deque

def in_range(v, x, y):
    return v>=x and v<=y

def can_go(v, x, y, step, varr):
    if not in_range(v, x, y):
        # print("not in range")
        return False
    if varr[v] != -1:
        # print("already visited")
        return False
    if varr[v] != -1 and varr[v] <= step:
        # print("step is too high")
        return False
    return True

q = deque()

def move(v, step, varr):
    q.append((v, step))
    varr[v] = step
    
def bfs(sv, ev, n, varr):
    move(sv, 0, varr)
    
    while q:
        v, step = q.popleft()
        
        if v == ev:
            return step
        
        for nv in [v+n, v*2, v*3]:
            if can_go(nv, sv, ev, step+1, varr):
                move(nv, step+1, varr)
                
    return -1

def solution(x, y, n):    
    visited = [
        -1 for _ in range(y+1)
    ]
    
    answer = bfs(x, y, n, visited)
    
    return answer
