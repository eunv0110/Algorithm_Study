def solution(my_strings, parts):
    answer=[]
    for idx,string in enumerate(my_strings):
        answer.append(string[parts[idx][0]:parts[idx][1]+1])
    return ''.join(answer)
    