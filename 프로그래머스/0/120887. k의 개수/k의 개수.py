def solution(i, j, k):
    num=''
    for i in range(i,j+1):
        num+=str(i)
    answer=num.count(str(k))
    return answer