for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    yasser = sum(a)
    neg = 0
    pos = 0
    happy = True
    for i in range(n):
        if a[i] > 0:
            pos += a[i]
        else:
            neg -= a[i]

        if neg >= pos:
            happy = False

    neg = 0
    pos = 0
    if happy:
        for i in range(n-1, -1, -1):
            if a[i] > 0:
                pos += a[i]
            else:
                neg -= a[i]
            if neg >= pos:
                happy = False

    if happy:
        print('YES')
    else:
        print('NO')
