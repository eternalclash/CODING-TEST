from itertools import product

def solution(users, emoticons):
    answer = []
    
    percentage = [10, 20, 30, 40]
    
    sale_list = list(product(percentage, repeat=len(emoticons)))
    
    for sales in sale_list:
        
        temp = [0, 0]
        
        for user in users:
            emoticon_plus, spend_money = 0, 0
            want_sale, want_money = user[0], user[1]

            for sale, emoticon in zip(sales, emoticons):
                if sale >= want_sale:
                    spend_money += emoticon * (1 - sale/100)

                    if spend_money >= want_money:
                        emoticon_plus = 1
                        spend_money = 0
                        break
                        
            temp[0] += emoticon_plus
            temp[1] += spend_money

        answer.append(temp)
    
    answer.sort(key = lambda x:(-x[0], -x[1]))
                
    return answer[0]
