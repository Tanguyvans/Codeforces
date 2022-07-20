for _ in range(int(input())):
    n, m = map(int, input().split())

    matrix = [[] for i in range(m)]
    for i in range(n):
        a = input()
        a = [j for j in a]
        for j in range(m):
            matrix[j].append(a[j])

    for mi in matrix:
        g = n-1
        for j in range(n-1, -1, -1):
            if mi[j] == 'o':
                g = j-1
            elif mi[j] == '*':
                mi[j] = '.'
                mi[g] = '*'
                g -= 1

    sol = [[] for i in range(n)]
    for i in range(m):
        for j in range(n):
            sol[j].append(matrix[i][j])

    for i in range(n):
        for j in range(m):
            print(sol[i][j], end='')
        print('')

    print('')
