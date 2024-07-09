def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        answer2=[]
        for j in range(len(arr1[i])):
            x=arr1[i][j]+arr2[i][j]
            answer2.append(x)
        answer.append(answer2)
    return answer
    
