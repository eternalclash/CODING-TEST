import heapq

def counter(arr):
    dd = {}
    for t in arr:
        if t in dd:
            dd[t] += 1
        else:
            dd[t] = 1
    return dd
            
def solution(k, tangerine):
    answer = 0
    
    dd = counter(tangerine)
    hq = []
    
    for d in counter(tangerine):
        heapq.heappush(hq, -dd[d])
    
    while hq:
        n = -heapq.heappop(hq)
                
        if k == 0:
            break
            
        if n > k:
            answer += 1
            break

        answer += 1
        k -= n
        
    return answer
