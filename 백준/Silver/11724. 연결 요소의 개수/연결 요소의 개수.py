import sys

# 재귀 깊이 설정 (예: 10**6)
sys.setrecursionlimit(10**6)
# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

n,m=map(int,input().split())
#그래프 초기화
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

#간선정보 입력
for _ in range(m):
  u,v=map(int,input().split())
  graph[u].append(v) #문제에서 양방향이라고 했으므로
  graph[v].append(u)

def dfs(v):
  visited[v]=True #방문처리
  for i in graph[v]: #방문하지 않은 경우 dfs 재귀적으로 불러오기
    if not visited[i]:
      dfs(i)

count=0
for i in range(1,n+1): #노드는 1번부터 있기 때문에
  if not visited[i]:
    dfs(i)
    count+=1

print(count)