def solution(s1, s2):
    s1.extend(s2)
    answer=len(list(set(s1)))
    return len(s1)-answer