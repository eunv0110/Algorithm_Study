def solution(numbers, direction):
    result=[]
    if direction=='right':
        result.append(numbers[-1])
        result.extend(numbers[:len(numbers)-1])
    if direction=='left':
        result.extend(numbers[1:len(numbers)])
        result.append(numbers[0])
    
    return result
        