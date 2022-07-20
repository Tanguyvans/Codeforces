for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    p = a[0]
    imp = False
    for i in range(1, n):
        if a[i] / p == int(a[i]/p) and a[i] >= p:
            pass
        else:
            imp = True
            break

    if imp:
        print('NO')
    else:
        print('YES')
