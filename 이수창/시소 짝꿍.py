from collections import defaultdict
def solution(weights):
    
    obj = defaultdict(int)
    answer = 0
    for weight in weights:
        obj[weight]+=1
    for key,val in obj.items():
        if val > 0 :
            answer += val*(val-1)/2
        if key * 2 in obj :
            answer += val * obj[key *2]
        if key * 3 / 2 in obj:
            answer += val * obj[key * 3 /2]
        if key * 4 / 3 in obj:
            answer += val * obj[key * 4 / 3]
    return answer




            
            