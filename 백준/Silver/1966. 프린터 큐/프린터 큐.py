from collections import deque

#테스트할 개수
T=int(input())

for _ in range(T):
  #문서의 개수 n, 놓여져있는 정수 m
  n,m=map(int,input().split(' '))
  #중요도
  importances=list(map(int,input().split(' ')))
  sorted_importances=deque(sorted(importances,reverse=True))
  documents=deque()
  for idx,importance in enumerate(importances):
    documents.append((idx,importance))

  count=0

  while documents:
    idx,importance=documents.popleft()

    if importance>=sorted_importances[0]:
      sorted_importances.popleft()
      count+=1

      if idx==m:
        print(count)
        break

    else:
      documents.append((idx,importance))    
