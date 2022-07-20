for _ in range(int(input())):
    n, m, r, c = map(int, input().split())

    grid = []
    for i in range(n):
        grid.append(list(input()))

    if grid[r-1][c-1] == 'B':
        print(0)
    elif 'B' in grid[r-1]:
        print(1)
    elif any(i[c-1] == 'B' for i in grid):
        print('1')
    elif any('B' in i for i in grid):
        print('2')
    else:
        print('-1')
