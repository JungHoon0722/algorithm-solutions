# (1) 함수 매개변수 순서 통일하기
# 좌표를 (x, y)로 받고 있는데, 파이썬 2D 리스트 인덱스는 campus[y][x] (행, 열 순)입니다.

# DFS 호출도 DFS(x, y)인데, 내부에서 visited[y][x] 등으로 행과 열을 뒤집어 쓰는 게 헷갈릴 수 있습니다.

# 보통 좌표는 (y, x) (행, 열) 순으로 일관시키는 게 가독성에 좋습니다.

# (2) visited 체크 위치
# 현재는 함수 첫 줄에 방문 여부를 검사하지만, DFS 진입 전에 체크하고 진입하는 게 더 일반적입니다.

# 즉, DFS 진입 직전에 방문 여부와 벽('X') 여부를 확인하면 불필요한 함수 호출을 줄일 수 있습니다.

# (3) 전역변수 대신 반환값 활용 (가독성 및 유지보수 향상)
# 전역 friends_count 대신 DFS 함수가 친구 수를 반환하도록 바꿀 수 있습니다.

# 이렇게 하면 전역 상태 관리가 줄고, 코드가 더 함수형에 가까워집니다.

# (4) 방향 배열 관리
# 현재 방향 배열은 (dx, dy)인데, 인덱스 기준과 혼용되어 헷갈릴 수 있습니다.

# (dy, dx)로 일관하면 더 직관적입니다.

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