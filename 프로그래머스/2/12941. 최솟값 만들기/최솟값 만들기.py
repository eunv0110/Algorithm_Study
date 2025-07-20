def solution(A,B):
    A=list(sorted(A))
    B=list(reversed(sorted(B)))
    answer=0
    for a,b in zip(A,B):
        answer+=a*b

    return answer