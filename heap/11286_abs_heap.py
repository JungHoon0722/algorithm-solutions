# 11286: 절댓값 힙
# 난이도: Silver 1
# 알고리즘 분류: Heap, Priority Queue
# 아이디어: heapq 사용해 (절댓값, 실제값)튜플 절댓값 기준 정렬
# 시간복잡도: [O(N log N)]

import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(x), x))