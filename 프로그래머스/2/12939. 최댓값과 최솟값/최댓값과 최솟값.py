def solution(s):
    s=list(sorted(map(int,s.split(' '))))
    min_num,max_num=str(min(s)),str(max(s))
    return min_num+' '+max_num