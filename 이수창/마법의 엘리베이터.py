def solution(cur):
    cnt = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
    answer = float('inf')
    
    def helper(cur, val):
        nonlocal answer
        if cur < 10:
            p = 1 if cur > 5 else 0
            answer = min(cnt[cur] + p + val, answer)
            return
        if cur % 10 <= 5:
            helper(cur // 10, cnt[cur % 10] + val)
        if cur % 10 >= 5:
            helper(cur // 10 + 1, cnt[cur % 10] + val)
    
    helper(cur, 0)
    return answer
