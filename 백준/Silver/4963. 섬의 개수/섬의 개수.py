from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 0  # 방문처리
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0  # 여기가 수정된 부분

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    count = 0
    
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                bfs(x, y)
                count += 1
    
    print(count)