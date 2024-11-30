from collections import deque

#수빈이가 있는 위치와 동생이 있는 위치
n,k=map(int,input().split())
MAX=100000
visited=[0]*(MAX+1)

def bfs(n):
  queue=deque([n])

  while queue:
    x=queue.popleft()
    #수빈이 위치가 동생 위치와 같다면 종료

    if x==k:
      return visited[x]
      
    for i in (x-1,x+1,x*2):
      #주어진 범위내에 있고 아직 방문하지 않았다면
      if 0<=i<=MAX and not visited[i]:
        #이동한 시간 표시
        visited[i]=visited[x]+1
        queue.append(i)

print(bfs(n))