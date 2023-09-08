def solution(storey):   
    list_storey = list(map(int, str(storey)))
    
    list_storey.reverse()
    list_storey.append(0)
    
    for i, elem in enumerate(list_storey):
        if i == len(list_storey)-1:
            break
            
        if elem > 5 or (elem == 5 and list_storey[i+1] >= 5):
            list_storey[i] = 10 - list_storey[i]
            list_storey[i+1] += 1
                
    return sum(list_storey)
  
