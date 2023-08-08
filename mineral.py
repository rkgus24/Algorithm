import sys
from collections import deque
CHANG_YOUNG, SANG_GEUN = 0, 1
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_R = 100

R, C = map(int, sys.stdin.readline().rstrip().split())
cave = []
for _ in range(R):
    cave.append(list(sys.stdin.readline().rstrip()))
N = int(sys.stdin.readline().rstrip())
H = list(map(int, sys.stdin.readline().rstrip().split()))

def throw_stick_from_left(h):
    for x in range(C):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def throw_stick_from_right(h):
    for x in range(C-1, -1, -1):
        if cave[h][x] == 'x':
            cave[h][x] = '.'
            return h, x
    return -1, -1

def print_cave():
    for row in cave:
        print(*row, sep='')

def get_cluster_visited(start_y, start_x):
    visited = [[False]*C for _ in range(R)]
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in DIRS:
            ny, nx = y+dy, x+dx
            if not (0 <= ny < R and 0 <= nx < C):
                continue
            if cave[ny][nx] == '.':
                continue
            if visited[ny][nx]:
                continue
            q.append((ny, nx))
            visited[ny][nx] = True
    return visited

def get_min_y_list(visited):
    min_y_list = [-1]*C
    for x in range(C):
        for y in range(R-1, -1, -1):
            if visited[y][x]:
                min_y_list[x] = y
                break
    return min_y_list
            
def get_fall_height(min_y_list):
    min_diff = MAX_R + 1
    for x, min_y in enumerate(min_y_list):
        if min_y == -1:
            continue
        for y in range(min_y + 1, R):
            if cave[y][x] == 'x':
                min_diff = min(min_diff, y - min_y - 1)
                break
            if y == R-1:
                min_diff = min(min_diff, y - min_y)
    return min_diff

def fall(h, visited):
    for y in range(R-1, -1, -1):
        for x in range(C):
            if not visited[y][x]:
                continue
            cave[y][x] = '.'
            cave[y+h][x] = 'x'

turn = CHANG_YOUNG
for h in H:
    h = R-h
    mineral_y, mineral_x = -1, -1
    if turn == CHANG_YOUNG:
        mineral_y, mineral_x = throw_stick_from_left(h)
        turn = SANG_GEUN
    else:
        mineral_y, mineral_x = throw_stick_from_right(h)
        turn = CHANG_YOUNG
    if (mineral_y, mineral_x) == (-1, -1):
        continue
    for dy, dx in DIRS:
        ny, nx = mineral_y + dy, mineral_x + dx
        if not (0 <= ny < R and 0 <= nx < C):
            continue
        if cave[ny][nx] == '.':
            continue
        visited = get_cluster_visited(ny, nx)
        min_y_list = get_min_y_list(visited)
        
        if R-1 in min_y_list:
            continue

        fall_height = get_fall_height(min_y_list)
        fall(fall_height, visited)

        break

print_cave()
