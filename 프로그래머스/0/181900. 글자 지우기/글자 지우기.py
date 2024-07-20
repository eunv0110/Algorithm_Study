def solution(my_string, indices):
    my_string=list(my_string)
    for idx in sorted(indices,reverse=True):
        del my_string[idx]
    return ''.join(my_string)
