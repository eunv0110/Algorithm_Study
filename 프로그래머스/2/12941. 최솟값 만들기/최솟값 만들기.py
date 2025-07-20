def solution(A,B):
    A=list(sorted(A))
    B=list(reversed(sorted(B)))
    answer=0
    for i in range(len(A)):
        answer+=A[i]*B[i]

    return answer