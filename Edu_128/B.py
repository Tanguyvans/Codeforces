for _ in range(int(input())):
    n, m = map(int, input().split(' '))

    mat = []
    for i in range(n):

        line = input()
        mat.append([i for i in line])

    if mat[0][0] == 'R':
        print('YES')
    else:
        upper = [5, 5]
        lefter = [5, 5]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 'R':
                    if upper[0] > i:
                        upper = [i, j]
                    elif upper[0] == i and upper[1] > j:
                        upper = [i, j]

                    if lefter[1] > j:
                        lefter = [i, j]
                    elif lefter[1] == j and lefter[0] > i:
                        lefter = [i, j]

        if upper == lefter:
            print('YES')
        else:
            print('NO')
