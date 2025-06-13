def solution(n, computers):
    
    visited=[False]*n
    count=0
    
    for i in range(n):
        if not visited[i]:
            dfs(i,computers,visited)
            count+=1
    

    return count

def dfs(node,computers,visited):
    
    visited[node]=True #방문처리
    

    for i in range(len(computers)):
        if computers[node][i]==1 and not visited[i]:
            dfs(i,computers,visited)
                