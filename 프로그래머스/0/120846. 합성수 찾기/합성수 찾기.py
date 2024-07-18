def solution(n):
    count=0
    for num in range(4,n+1):
        divisors=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                divisors+=1
                if i!=num//i:
                    divisors+=1
            if divisors>=3:
                count+=1
                break
        
    return count
            
        