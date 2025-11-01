def solution(n, times):
    end=n*max(times)
    start=0
    answer = 0
    
    while start<=end:
        total=0
        if start>end:
            break
        
        mid=(start+end)//2
        
        for time in times:
            total+=mid//time
        
        if total>=n:
            end=mid-1
            answer=mid
        else:
            start=mid+1
        
        
    return answer