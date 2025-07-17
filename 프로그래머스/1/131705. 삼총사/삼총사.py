from itertools import combinations
def solution(number):
    count=0
    nums=list(combinations(number,3))
    for num in nums:
        if sum(num)==0:
            count+=1
            
    return count