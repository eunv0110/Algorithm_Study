def solution(t, p):
    nums=[]
    for i in range(len(t)-len(p)+1):
        result=t[i:i+len(p)]
        nums.append(int(result))
    
    answer=0
    print(nums)
    
    for num in nums:
        if num <= int(p):
            answer+=1
    return answer
        
