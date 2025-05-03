from collections import deque
import sys

m, n = map(int, sys.stdin.readline().strip().split())  # m: 가로, n: 세로
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]  # 좌우
dy = [0, 0, -1, 1]  # 상하

def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))

bfs()

result = 0
for row in box:
    if 0 in row:
        print(-1)
        break
    result = max(result, max(row))
else:
    print(result - 1)
