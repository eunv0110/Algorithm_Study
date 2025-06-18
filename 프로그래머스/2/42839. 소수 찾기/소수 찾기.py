from itertools import permutations
def solution(numbers):
    nums=[]
    numbers = list(map(int,list(numbers)))
    count=0
    
    for i in range(1,len(numbers)+1):
        
        perm=set(list(permutations(numbers,i)))
        print(perm)
        
        for num in perm:
            n=''.join(map(str,num))
            nums.append((int(n)))
    nums=list(set(nums))
    
    for num in nums:
        if is_Prime(int(num)):
            count+=1
    return count
        

def is_Prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        
        if n%i==0:
            return False
        
        
    return True


            