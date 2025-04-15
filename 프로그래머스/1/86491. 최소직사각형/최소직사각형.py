def solution(sizes):
    answer1=[]
    answer2=[]
    for size in sizes:
        if size[0]<size[1]:
            size[0],size[1]=size[1],size[0]
        answer1.append(size[0])
        answer2.append(size[1])
        answer1.sort()
        answer2.sort()
        
    return answer1[-1]*answer2[-1]