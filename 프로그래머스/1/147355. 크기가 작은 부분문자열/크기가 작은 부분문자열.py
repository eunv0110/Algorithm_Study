def solution(t, p):
    count=0
    int_p=int(p)
    for i in range(len(t)-len(p)+1):
        sub_str=t[i:i+len(p)]
        if int_p>=int(sub_str):
            count+=1
    return count