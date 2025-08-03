from collections import deque
def solution(maps):
    answer= bfs(maps,0,0)
    if answer==1:
        return -1
    return answer
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(maps,y,x):
    queue=deque([(y,x)])
    
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                if maps[ny][nx]==1:
                    maps[ny][nx]=maps[y][x]+1
                    queue.append((ny,nx))
    return maps[-1][-1]