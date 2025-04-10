from itertools import *

def solution(before, after):
    before=sorted(list(before))
    after=sorted(list(after))
    
    if before==after:
        return 1
    else:
        return 0
