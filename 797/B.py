for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    c = [[a[i], b[i]] for i in range(n)]

    c = sorted(c, key=lambda c: [-c[1], c[0]])

    flag = False
    ecart = -1
    for i in range(n):
        if ecart == -1:
            if c[i][1] == 0:
                break

            elif c[i][0]-c[i][1] < 0:
                flag = True
                break
            else:
                ecart = c[i][0]-c[i][1]

        else:
            if c[i][0] - c[i][1] < ecart and c[i][1] != 0:
                flag = True
                break
            elif c[i][0] - c[i][1] > ecart:
                flag = True
                break

    if flag:
        print('NO')
    else:
        print('YES')
