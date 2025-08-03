def solution(s):
    
    stack=[]
    
    for i in s:
        if i=="(":
            stack.append(i)
        elif i==')':
            if not stack:
                print(len(stack))
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True