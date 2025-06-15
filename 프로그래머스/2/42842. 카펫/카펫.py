def solution(brown, yellow):
    total=brown+yellow
    #약수의 리스트를 구하자
    nums=[]
    
    for num in range(1,int(total**0.5)+1):
        if total%num==0:
            nums.append((total//num,num))
    
    for w,h in nums:
        
        if yellow==(w-2)*(h-2):
            return [w,h]
            
