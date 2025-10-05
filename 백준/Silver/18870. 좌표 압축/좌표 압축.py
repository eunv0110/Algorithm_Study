from bisect import bisect_left

n=int(input())
array=list(map(int,input().split(' ')))

sorted_array=list(sorted(set(array)))

answer=[bisect_left(sorted_array,a) for a in array]

print(' '.join(map(str,answer)))

