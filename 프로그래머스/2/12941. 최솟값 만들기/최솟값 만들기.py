def solution(A,B):
    A=sorted(A)
    B=list(reversed(sorted(B)))
    answer=[]
    for i in range(len(A)):
        answer.append(A[i]*B[i])
        
    return sum(answer)