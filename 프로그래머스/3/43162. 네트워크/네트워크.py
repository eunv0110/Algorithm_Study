from collections import deque

def solution(n, computers):
    #방문노드 설정
    
    visited=[False]*n
    count=0
    
    for i in range(n):
        if not visited[i]:
            print(i,': 새 네트워크 탐색')
            bfs(i,computers,visited)
            count+=1
    return count

def bfs(start, computers,visited):
    
    queue=deque([start])
    visited[start]=True #방문처리
    print(start,"큐에 추가(방문표시)")
    
    while queue:
        
        node=queue.popleft()
        print(f"노드 {node} 탬색 중, 연결상태 {computers[node]}")
        
        for i in range(len(computers[node])):
                        
            if computers[node][i]==1 and not visited[i]:
                print(i,"연결됨!큐에 추가하고 방문표시")

                visited[i]=True #방문처리
                queue.append(i)
    
    
    