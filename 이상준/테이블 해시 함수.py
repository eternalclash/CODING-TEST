def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key = lambda x:(x[col-1], -x[0]))
    
    stack = []
    
    for i, d in enumerate(data, start=1):
        temp = 0
        for elem in d:
            temp += elem%i
        stack.append(temp)
    
    for s in stack[row_begin-1: row_end]:
        answer ^= s
        
    return answer
