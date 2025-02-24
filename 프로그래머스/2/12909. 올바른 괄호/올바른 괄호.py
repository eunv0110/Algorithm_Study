def solution(s):
    stack=[]
    
    for char in s:
        if char=='(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop() #올바른 경우 짝을 경우
    return not stack

