#컴퓨터의 수
n=int(input())

#컴퓨터 쌍의 수
m=int(input())

#그래프
graph=[[] for _ in range(n+1)]
#방문노드
visited=[False]*(n+1)

#간선의 정보
for _ in range(m):
  u,v=map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

#dfs로 풀거야
def dfs(v,group):
  visited[v]=True
  group.append(v)
  for i in graph[v]:
    if not visited[i]:
      dfs(i,group)

groups=[]
for i in range(1,n+1):
  if not visited[i]:
    group=[]
    dfs(i,group)
    groups.append(group)

for group in groups:
  if 1 in group:
    group.remove(1)
    print(len(group))