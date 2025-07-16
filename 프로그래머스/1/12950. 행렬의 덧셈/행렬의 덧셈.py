def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        nums=[]
        for j in range(len(arr1[0])):
            nums.append(arr1[i][j]+arr2[i][j])
        answer.append(nums)
    return answer

