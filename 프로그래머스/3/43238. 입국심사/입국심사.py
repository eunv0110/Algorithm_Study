def solution(n, times):
    answer = 0
    start=1
    end=max(times)*n
    
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