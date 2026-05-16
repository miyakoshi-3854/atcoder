h, w = map(int, input().split())

grid = [[4 for _ in range(w)] for _ in range(h)]

for y in range(h):
    for x in range(w):
        if y == 0:
            grid[y][x] -= 1
        if y == h - 1:
            grid[y][x] -= 1
        if x == 0:
            grid[y][x] -= 1
        if x == w - 1:
            grid[y][x] -= 1

for row in grid:
    print(" ".join(map(str, row)))
