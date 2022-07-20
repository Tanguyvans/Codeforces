for _ in range(int(input())):
    n, x = map(int, input().split())

    a = list(map(int, input().split()))
    a = sorted(a)
    imp = False
    for i in range(n):
        if a[i] + x > a[i+n]:
            imp = True
            break

    if imp:
        print('NO')
    else:
        print('YES')
