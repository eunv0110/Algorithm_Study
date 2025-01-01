from collections import deque

N = int(input())
picture = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    color = list(input())
    picture.append(color)

visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

def bfs(x, y, visited, grid):
    queue = deque()
    queue.append((x, y))
    color = grid[x][y]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 범위를 벗어났거나 방문했을 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue
            if grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 적록색맹용 그림 생성 (깊은 복사)
picture2 = [row[:] for row in picture]
for i in range(N):
    for j in range(N):
        if picture2[i][j] == 'G':
            picture2[i][j] = 'R'

count = 0
count2 = 0

# 일반 그림 탐색
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, visited, picture)
            count += 1

# 색맹 그림 탐색
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            bfs(i, j, visited2, picture2)
            count2 += 1

print(count, count2)
