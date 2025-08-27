# 2667: 단지번호붙이기
# 난이도: Silver 1
# 알고리즘 분류: BFS, Graph
# 아이디어: 2D 배열에서 BFS 탐색 후 단지별 집 수 카운트
# 시간복잡도: [O(N^2)]

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

complexes = []

def BFS(y, x):
    queue = deque()
    visited[y][x] = True
    queue.append((y, x))
    count = 0

    while queue:
        count += 1
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if home[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    
    return count

for y in range(N):
    for x in range(N):
        if home[y][x] and not visited[y][x]:
            complexes.append(BFS(y, x))

complexes.sort()
print(len(complexes))
for i in complexes:
    print(i)