def solution(n, wires):
    def dfs(v,skip_v1,skip_v2):
        visited[v]=True
        count=1
        for i in graph[v]:
            if (v==skip_v1 and i==skip_v2) or (v==skip_v2 and i==skip_v1):
                continue
            if not visited[i]:
                count+=dfs(i,skip_v1,skip_v2)
        return count
    
    answer=n
    
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for skip_v1,skip_v2 in wires:
        visited=[False]*(n+1)
        #간선하나 끊고 수행
        count=dfs(1,skip_v1,skip_v2)
        other=n-count
        
        answer=min(answer,abs(count-other))
        
    return answer
            
    
    
