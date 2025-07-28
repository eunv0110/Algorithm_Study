from itertools import combinations
from collections import defaultdict

def solution(clothes):
    
    clothes_dict=defaultdict(list)
    
    for cloth,kind in clothes:
        clothes_dict[kind].append(cloth)
        
    all_case=1
    
    for kind in clothes_dict:
        all_case*=(len(clothes_dict[kind])+1)
    
    return all_case-1
