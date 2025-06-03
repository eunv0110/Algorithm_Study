def solution(numbers, target):
    answer = 0
    
    def dfs(current_num,idx):
        nonlocal answer
        #모든 숫자를 다 골랐을때
        if idx==len(numbers):
        #타겟값이랑 현재값이랑 같으면 answer+1
            if target==current_num:
                answer+=1 
            return 
        
        dfs(current_num+numbers[idx],idx+1)
        dfs(current_num-numbers[idx],idx+1)
    dfs(0,0)
    return answer