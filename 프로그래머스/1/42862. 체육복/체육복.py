def solution(n, lost, reserve):
    #교집합 먼저 제거
    lost=set(lost)
    reserve=set(reserve)
    
    overlap=lost&reserve
    reserve-=overlap
    lost-=overlap
    print(reserve)
    print(lost)
    
    for r in sorted(reserve):
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n-len(lost)
