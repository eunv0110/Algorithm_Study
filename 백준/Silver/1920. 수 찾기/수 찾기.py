from bisect import bisect_right,bisect_left

n=int(input())
arr=list(sorted(map(int,input().split(' '))))
m=int(input())
nums=list(map(int,input().split(' ')))
for num in nums:
  idx=bisect_left(arr,num)
  if idx < n and arr[idx] == num:
    print(1)
  else:
    print(0)