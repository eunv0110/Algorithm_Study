from bisect import bisect_left

n=int(input())
array=list(map(int,input().split(' ')))

sorted_array=list(sorted(set(array)))
answer=[]

for a in array:
  left_index=bisect_left(sorted_array,a)
  answer.append(left_index)

print(' '.join(map(str,answer)))