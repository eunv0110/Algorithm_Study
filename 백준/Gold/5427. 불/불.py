from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solve():
  w,h=map(int,input().split(' '))
  graph=[list(input()) for _ in range(h)]

  fire_time=[[-1]*w for _ in range(h)]
  person_time=[[-1]*w for _ in range(h)]

  fq,pq=deque(),deque()

  for y in range(h):
    for x in range(w):
      if graph[y][x]=='*':
        fq.append((y,x))
        fire_time[y][x]=0
      elif graph[y][x]=='@':
        pq.append((y,x))
        person_time[y][x]=0

  while fq:
    y,x=fq.popleft()

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if 0<=nx<w and 0<=ny<h:
        if fire_time[ny][nx]==-1 and graph[ny][nx]=='.':
          fq.append((ny,nx))
          fire_time[ny][nx]=fire_time[y][x]+1
  while pq:
    y,x=pq.popleft()

    if y==0 or y==h-1 or x==0 or x==w-1:
      print(person_time[y][x]+1)
      return

    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if 0<=nx<w and 0<=ny<h:
        if graph[ny][nx]=='.' and person_time[ny][nx]==-1:
          nt=person_time[y][x]+1
          if fire_time[ny][nx]==-1 or fire_time[ny][nx]>nt:
            pq.append((ny,nx))
            person_time[ny][nx]=nt
  print("IMPOSSIBLE")

t=int(input())
for _ in range(t):
  solve()
