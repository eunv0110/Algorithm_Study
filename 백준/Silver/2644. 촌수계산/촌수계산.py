#사람들 명수
p=int(input())

#촌수 계산
p1,p2=map(int,input().split())

#그래프 선언
graph=[[] for _ in range(p+1)] #1로 시작하기 때문에
#방문그래프
visited=[False]*(p+1)

#간선의 개수
v=int(input())

#부모 자식 간의 관계
for _ in range(v):
  x,y=map(int,input().split())
  #양방향이므로
  graph[x].append(y)
  graph[y].append(x)

def dfs(v,count):
  if v==p2: #목표 노드에 도달하면 촌수 반환
    return count
  visited[v]=True #방문처리
  
  for i in graph[v]:
    if not visited[i]:
      result=dfs(i,count+1)
      if result!=-1:
        return result
      
  return -1


print(dfs(p1,0))
