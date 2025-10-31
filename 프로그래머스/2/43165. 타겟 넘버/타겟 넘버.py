def solution(numbers, target):
    answer = 0
    
    def recur(idx,total):
        nonlocal answer
        
        if idx==len(numbers):
            if target==total:
                answer+=1
            return
        recur(idx+1,total+numbers[idx])
        recur(idx+1,total-numbers[idx])
    
    recur(0,0)
    return answer

