def solution(sizes):
    
    size1=0
    size2=0
    
    for a,b in sizes:
        
        if b>a:
            b,a=a,b
        
        size1=max(size1,b)
        size2=max(size2,a)

    return size1*size2