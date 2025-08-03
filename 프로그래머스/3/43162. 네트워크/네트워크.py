from collections import deque

def solution(n, computers):
    visited=[False]*n
    answer=0
    for i in range(n):
        if not visited[i]:
            dfs(i,computers,visited)
            answer+=1
    return answer

def dfs(node,computers,visited):
    
    visited[node]=True
        
    for i in range(len(computers[0])):
        if computers[node][i]==1 and not visited[i]:
            dfs(i,computers,visited)