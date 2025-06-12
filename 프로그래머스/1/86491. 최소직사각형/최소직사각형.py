def solution(sizes):
    
    size1=0
    size2=0
    
    for size in sizes:
        size.sort(reverse=True)
        size1=max(size1,size[0])
        size2=max(size2,size[1])

    
    
    return size1*size2