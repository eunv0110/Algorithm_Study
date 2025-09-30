from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

icebergs = set()
#빙산의 좌표
for y in range(n):
  for x in range(m):
    icebergs.add((y,x))

#bfs로 빙산 덩어리 개수세기

def bfs(icebergs):

  visited=set()
  components=0

  for start in icebergs:
    if start not in visited:
      components+=1
      queue=deque([start])
      visited.add(start)

      while queue:
        y,x=queue.popleft()

        for i in range(4):
          nx=x+dx[i]
          ny=y+dy[i]

          if (ny,nx) in icebergs and (ny,nx) not in visited:
            visited.add((ny,nx))
            queue.append((ny,nx))
  return components

def melt_ice(icebergs):
  melt={}

  for y,x in icebergs:
    sea=0

    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      
      if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
        sea+=1
      melt[(y,x)]=sea

  new_icebergs=set()
  for (y,x),value in melt.items():
    graph[y][x]=max(0,graph[y][x]-value)

    if graph[y][x]>0:
      new_icebergs.add((y,x))
  return new_icebergs

year=0

while True:

  if not icebergs:
    print(0)
    break
  
  count=bfs(icebergs)
  if count>=2:
    print(year)
    break
  
  icebergs=melt_ice(icebergs)
  year+=1

