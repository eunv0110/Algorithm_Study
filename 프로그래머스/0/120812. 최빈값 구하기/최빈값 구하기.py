def solution(array):
    answer=[]
    freq={}
    
    for num in array:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    max_freq=max(freq.values())
    
    for num,count in freq.items():
        if count==max_freq:
            answer.append(num)

    if len(answer)>1:
        return -1
    else:
        return answer[0]

        