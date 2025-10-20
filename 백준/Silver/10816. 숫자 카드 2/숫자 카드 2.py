from bisect import bisect_right,bisect_left
#상근이가 가지고 있는 숫자 카드 개수
n=int(input())
nums=list(sorted(map(int,input().split(' '))))
m=int(input())
cards=list(map(int,input().split(' ')))
answer=[]

for card in cards:

  right=bisect_right(nums,card)
  left=bisect_left(nums,card)


  answer.append(right-left)

print(' '.join(map(str,answer)))