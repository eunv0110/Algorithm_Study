def solution(num, k):
    num=str(num)
    answer=num.find(str(k))
    if answer<0:
        return -1
    else:
        return answer+1
