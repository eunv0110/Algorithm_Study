from bisect import bisect_right,bisect_left
#상근이가 가지고 있는 카드의 개수
n=int(input())
cards=list(sorted(map(int,input().split(' '))))
m=int(input())
nums=list(map(int,input().split(' ')))

def count_by_cards(num):
  right_index=bisect_right(cards,num)
  left_index=bisect_left(cards,num)

  return right_index-left_index

answer=[]
for num in nums:
  total=0
  answer.append(count_by_cards(num))

print(' '.join(map(str,answer)))
  
