def solution(array, commands):
    result = []
    for command in commands:
        
        x,y,z=command
        slice_array=array[x-1:y]
        slice_array.sort()
        result.append(slice_array[z-1])
    
    return result