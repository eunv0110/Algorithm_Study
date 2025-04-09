def solution(box, n):
    answer=1
    for b in box:
        x=b//n
        answer*=x
    return answer