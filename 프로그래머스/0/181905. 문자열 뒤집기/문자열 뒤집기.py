def solution(my_string, s, e):
    string=list(my_string[s:e+1])
    string.reverse()
    reversed_string=''.join(string)
    return my_string.replace(my_string[s:e+1],reversed_string)