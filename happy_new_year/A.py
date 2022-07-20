m = int(input())

for _ in range(m):
    n, k = map(int, input().split())

    inter = n
    for i in range(k):
        if i == k-1:
            inter -= 1
        else:
            inter -= 2

    if inter < 0:
        print(-1)

    else:
        grid = [['.' for j in range(n)]for i in range(n)]

        for i in range(n):
            if k > 0 and i % 2 == 0:
                grid[i][i] = 'R'
                k -= 1

        for i in grid:
            for j in i:
                print(j, end='')
            print('')
