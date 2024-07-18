def solution(strings):
    result=[]
    for string in strings:
        for i in range(len(string)):
            if result.count(string[i])==0:
                result.append(string[i])
    return ''.join(result)
            