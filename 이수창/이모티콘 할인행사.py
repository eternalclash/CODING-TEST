def solution(users, emoticons):
    percents = [10,20,30,40]
    cases = []
    arr = [0] * len(emoticons)
    answer = [0,0]
    def dfs (depth = 0) :
        if depth == len(emoticons):
            cases.append(arr.copy())
            return
        else:
            for percent in percents :
                arr[depth] = percent
                dfs(depth+1)
    dfs()
    for c in cases:
        totalService = 0
        totalMoney = 0
        for user in users:
            checkService = False
            userPercent = user[0]
            userMoney = user[1]
            sellMoney = 0
            for i in range(len(c)):
                if c[i] >= userPercent:
                    discountMoney = emoticons[i] * (100-c[i]) // 100
                    if discountMoney >= userMoney :
                        checkService = True
                        break
                    else :
                        userMoney -= discountMoney
                        sellMoney += discountMoney
            if checkService :
                totalService += 1
            else:
                totalMoney += sellMoney
        if totalService > answer[0] :
            answer[0] = totalService
            answer[1] = totalMoney
        if totalService == answer[0] :
            answer[1] = max(answer[1],totalMoney)
                
    return answer