import heapq

def solution(n, k, enemy):   
    hq = []
    
    for i, e in enumerate(enemy, start=1):
        if len(hq) < k:
            heapq.heappush(hq, e)
            continue
        
        temp = heapq.heappop(hq)
        if temp < e:
            n -= temp
            heapq.heappush(hq, e)
        else:
            n -= e
            heapq.heappush(hq, temp)
            
        if n < 0:
            i -= 1
            break
        
    return i
