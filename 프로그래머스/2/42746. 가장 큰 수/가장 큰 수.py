def solution(numbers):
    numbers=list(map(str,numbers))
    sorted_numbers=sorted(numbers,key=lambda number : number*4,reverse=True)
    
    return str(int(''.join(sorted_numbers)))
