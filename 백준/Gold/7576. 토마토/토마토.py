from collections import deque
import sys

m, n = map(int, sys.stdin.readline().strip().split())  # m: 열, n: 행

box = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    tomato = list(map(int, sys.stdin.readline().strip().split()))
    box.append(tomato)

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))

bfs()

# 결과 계산
result = 0
for row in box:
    if 0 in row:
        print(-1)
        break
    result = max(result, max(row))
else:
    print(result - 1)
