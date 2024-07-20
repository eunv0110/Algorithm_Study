from collections import Counter
def solution(strArr):
    answers=[]
    for arr in strArr:
        answers.append(len(arr))
    len_fre=Counter(answers)
    return len_fre.most_common(1)[0][1]
            