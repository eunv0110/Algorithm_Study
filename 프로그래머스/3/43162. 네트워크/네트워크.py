def solution(n, computers):
    visited=[False]*n
    answer = 0

    for node in range(n):
        if not visited[node]:
            dfs(node,computers,visited)
            answer+=1
    return answer

def dfs(node, computers,visited):
    visited[node]=True
    for next_node in range(len(computers)):
        if computers[node][next_node]==1 and not visited[next_node]:
            dfs(next_node, computers, visited)  # 재귀 호출
