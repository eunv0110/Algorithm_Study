def solution(my_string):
    my_string=list(my_string)
    answer=0
    for string in my_string:
        if string in ["1","2","3","4","5","6","7","8","9"]:
            answer+=int(string)
        
    return answer