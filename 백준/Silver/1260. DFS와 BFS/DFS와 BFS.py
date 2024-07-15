from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort()

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited1[neighbor]:
            dfs(neighbor)

def bfs(v):
    queue = deque([v])
    visited2[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in graph[current]:
            if not visited2[neighbor]:
                queue.append(neighbor)
                visited2[neighbor] = True

dfs(V)
print()  
bfs(V)