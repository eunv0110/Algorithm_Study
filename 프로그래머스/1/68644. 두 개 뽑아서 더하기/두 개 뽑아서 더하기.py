from itertools import combinations

def solution(numbers):
    nums = list(combinations(numbers,2))
    answer=set()
    for num in nums:
        answer.add(sum(num))
    answer=sorted(list(answer))
    return answer