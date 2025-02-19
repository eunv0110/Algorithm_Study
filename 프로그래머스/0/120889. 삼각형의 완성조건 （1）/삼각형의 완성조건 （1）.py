def solution(sides):
    sides=list(sorted(sides))
    return 2 if sides[2]>=sides[0]+sides[1] else 1
