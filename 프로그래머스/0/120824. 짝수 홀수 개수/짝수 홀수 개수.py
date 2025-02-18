def solution(num_list):
    even=[]
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            even.append(num_list[i])
    
    answer = []
    answer.append(len(even))
    answer.append(len(num_list)-len(even))
    return answer