for _ in range(int(input())):
    n, m = map(int, input().split())

    ti = 0
    li = m
    hi = m
    imp = False
    for i in range(n):
        t, l, h = map(int, input().split())

        hi += t - ti
        li -= t - ti

        if hi < l or li > h:
            imp = True

        hi = min(hi, h)
        li = max(li, l)

        ti = t

    if imp:
        print('NO')
    else:
        print('YES')
