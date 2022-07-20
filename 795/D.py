for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    a0 = 0
    sa = 0
    flag = False
    for i in range(n):
        sa += a[i]
        if a[i] > 0:
            if max(a[i], a0) < sa:
                flag = True
                break
            else:
                a0 = a[i]
                sa = a0

    if flag:
        print('NO')
    else:
        print('YES')
