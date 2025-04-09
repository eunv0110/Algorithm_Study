def solution(order):
    order=list(str(order))
    count=0
    for o in order:
        if o in ['3','6','9']:
            count+=1
    return count