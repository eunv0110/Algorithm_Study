def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row=[]
        for j in range(len(arr1[i])):
            x=arr1[i][j]+arr2[i][j]
            row.append(x)
        answer.append(row)
    return answer
