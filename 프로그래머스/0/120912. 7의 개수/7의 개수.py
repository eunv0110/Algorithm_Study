def solution(array):
    result=0
    for i in range(len(array)):
        array[i]=str(array[i])
        result+=array[i].count('7')
        
    return result