from collections import deque

def solution(numbers, target):
    answer = 0    
    queue=deque([(0,0)])
    
    while queue:
        
        current_num,idx=queue.popleft()
        
        if idx==len(numbers):
            if current_num==target:
                answer+=1
        else:
            queue.append((current_num+numbers[idx],idx+1))
            queue.append((current_num-numbers[idx],idx+1))
    return answer
