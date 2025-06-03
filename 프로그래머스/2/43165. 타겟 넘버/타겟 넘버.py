from collections import deque

def solution(numbers, target):
    queue=deque([(0,0)])
    answer = 0
    
    while queue:
        
        current_num,idx=queue.popleft()
        
        #모든 숫자를 다 돌았다면
        if idx==len(numbers):
            if current_num==target:
                answer+=1
        
        #그게 아니라면
        else:
            queue.append((current_num+numbers[idx],idx+1))
            queue.append((current_num-numbers[idx],idx+1))
       
    return answer
        
    