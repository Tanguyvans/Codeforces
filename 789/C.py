for _ in range(int(input())):

    n = int(input())
    p = list(map(int, input().split(' ')))

    mat = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):

            if p[i] > p[j]:
                mat[i][j] = 1
            elif p[i] == p[j]:
                mat[i][j] = 0
            else:
                mat[i][j] = -1

    ans = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == -1 and i+1 < j:
                pass
