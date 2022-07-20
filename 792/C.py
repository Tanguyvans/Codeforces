for _ in range(int(input())):

    n, m = map(int, input().split(' '))

    matrix = []

    for i in range(n):

        matrix.append(list(map(int, input().split(' '))))

    print(matrix)
    a = 0
    ai = 0
    b = 0
    flag = False

    for i in range(m):
        f2 = False
        for j in range(1, n):
            if matrix[i][j-1] > matrix[i][j]:
                if a == 0:
                    a = j
                    ai = matrix[i][j-1]
                    if j > 2:
                        if matrix[i][j-2] > matrix[i][j]:
                            flag = True
                            break
                    f2 = True
                else:
                    flag = True
                    break

            if f2:
                if
                if matrix[i][j]
