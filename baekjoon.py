import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([(0, 0)])
dist[0][0] = 1

while queue:
    r, c = queue.popleft()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if dist[nr][nc] == -1 and maze[nr][nc] == 1:
                dist[nr][nc] = dist[r][c] + 1
                if nr == N - 1 and nc == M - 1:
                    print(dist[nr][nc])
                    exit()
                queue.append((nr, nc))