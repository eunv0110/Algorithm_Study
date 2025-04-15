from itertools import permutations
def solution(k, dungeons):
    cases=list(permutations(dungeons))
    cases.sort(reverse=True)
    max_count=0
    for case in cases:
        remaining_k=k
        count=0
        for i in range(len(case)):
            if case[i][0]>remaining_k:
                continue
            count+=1
            remaining_k-=case[i][1]
        max_count=max(count,max_count)
    
    return max_count