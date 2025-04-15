from itertools import permutations

def solution(numbers):
    nums=set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            num=int(''.join(p))
            nums.add(num)
    count=0
    
    for num in nums:
        is_Prime=True
        if num<2:
            is_Prime=False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_Prime=False    
        if is_Prime==True:
            count+=1
    return count