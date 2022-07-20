for _ in range(int(input())):
    n = int(input())
    matrix = [list(input()) for i in range(n)]

    imp = False
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1':
                if i == n-1 or j == n-1:
                    pass
                elif matrix[i+1][j] == '1' or matrix[i][j+1] == '1':
                    pass
                else:
                    imp = True
                    break

    if imp:
        print('NO')
    else:
        print('YES')
