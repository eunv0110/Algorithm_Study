from collections import deque

n,k=map(int,input().split())
queue=deque([i for i in range(1,n+1)])
answer=[]
while queue:
  queue.rotate(-(k-1))
  node=queue.popleft()
  answer.append(node)

print('<'+', '.join(map(str,answer))+'>')