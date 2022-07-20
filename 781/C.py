for _ in range(int(input())):

    n = int(input())
    deg = [0 for i in range(n)]

    for i in list(map(int, input().split(' '))):
        deg[i-1] += 1

    a = [1]
    for i in deg:
        if i != 0:
            a.append(i)

    a = sorted(a, reverse=True)
    l = len(a)
    r = n

    while l < r:
        x = (l+r)//2
        cnt = 0
        for i in range(len(a)):
            cnt += max(0, a[i] - x + i)

        if len(a)+cnt <= x:
            r = x
        else:
            l = x + 1

    print(l)
