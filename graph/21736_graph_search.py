import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx)

def DFS(y, x):
    visited[y][x] = True
    count = 1 if campus[y][x] == 'P' else 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and campus[ny][nx] != 'X':
                count += DFS(ny, nx)
    return count

# 'I' 위치 찾기
start_y, start_x = None, None
for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            start_y, start_x = y, x
            break
    if start_y is not None:
        break

friends_count = DFS(start_y, start_x)
print(friends_count if friends_count > 0 else 'TT')