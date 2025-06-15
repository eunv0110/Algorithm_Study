def solution(n):
    
    nums=set()
    
    for num in range(1,int(n**0.5)+1):
        if n%num==0:
            nums.add(num)
            nums.add(n//num)

    return sum(nums)