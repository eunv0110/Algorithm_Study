from collections import deque

#테스트케이스 수
T=int(input())

for _ in range(T):
  #n: 문서의 개수, m : 몇번째로 놓여있는지 나타내는 정수
  n,m=map(int,input().split(' '))

  #문서 중요도 입력받기
  importance=list(map(int,list(input().split(' '))))
  sorted_importance=list(sorted(importance,reverse=True))

  queue=deque()
  for idx,document in enumerate(importance):
    queue.append((idx,document))
  count=0

  while queue:
    idx,importance=queue.popleft()

    if importance==sorted_importance[0]:
      sorted_importance.pop(0)
      count+=1

      if idx==m:
        print(count)
        break

    else:
      queue.append((idx,importance))

