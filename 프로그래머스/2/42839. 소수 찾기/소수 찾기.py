from itertools import permutations

def solution(numbers):
    
    answers=set()
    
    for i in range(1,len(numbers)+1):
        perm=list(permutations(numbers,i))
    
        for num in perm:
            answer=''.join(num)

            if is_Prime(int(answer)):
                answers.add(int(answer))
    
    return len(answers)
        

def is_Prime(num):
    
    if num<2:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    
    return True
    
        
        
        
        
    
