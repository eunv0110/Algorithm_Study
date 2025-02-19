def solution(array, height):
    array = list(sorted(array))
    count=0
    for i in range(len(array)):
        if array[i]>height:
            count+=1
    return count