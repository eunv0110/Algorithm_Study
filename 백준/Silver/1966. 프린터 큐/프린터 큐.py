from collections import deque

T=int(input())

for _ in range(T):
  #문서의 개수 n , 궁금한 문서 m
  n,m=map(int,input().split(' '))
  queue=deque()

  #중요도
  importances=list(map(int,input().split(' ')))

  #중요도 정렬
  sorted_importances=deque(list(sorted(importances,reverse=True)))

  for idx,importance in enumerate(importances):
    queue.append((idx,importance))

  count=0

  while queue:
    idx,importance=queue.popleft()

    if importance>=sorted_importances[0]:
      sorted_importances.popleft()
      count+=1
      if idx==m:
        print(count)
        break
    else:
      queue.append((idx,importance))
