def solution(left, right):
    
    answer=0
    
    for num in range(left,right+1):
        nums=set()
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                nums.add(i)
                nums.add(num//i)
        print(list(nums))
        if len(list(nums))%2==0:
            answer+=num
        else:
            answer-=num
                
        
    return answer