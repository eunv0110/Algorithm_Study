def solution(prices):
    answer=[0]*len(prices)
    stack=[]
    
    for i in range(len(prices)):
        #현재 값이 최근 값보다 작으면
        while stack and prices[i]<prices[stack[-1]]:
            #stack에 있는 값 하나 빼기
            j=stack.pop()
            answer[j]=i-j
        stack.append(i)
    
    #끝까지 다 돌았는데..
    while stack:
        j=stack.pop()
        answer[j]=len(prices)-j-1
            
    return answer