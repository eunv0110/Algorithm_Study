def solution(sizes):
    w_list=[]
    h_list=[]
    for size in sizes:
        size.sort(reverse=True)
    for i in range(len(sizes)):
        w_list.append(sizes[i][0])
        h_list.append(sizes[i][1])
    
    width=max(w_list)*max(h_list)
    return width
    