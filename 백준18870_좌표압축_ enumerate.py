import sys
input = sys.stdin.readline

N = int(input())
coordinates = list(map(int, input().strip().split()))
unique_coords = sorted(set(coordinates))
coords_dict = {num: idx for idx, num in enumerate(unique_coords)}

print(' '.join(str(coords_dict[i]) for i in coordinates))