for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = {i: 0 for i in range(1, n+1)}
    for i in a:
        d[i] += 1

    l = 1
    u = m

    while l < u:
        inter = (l+u)//2
        z = inter*1
        extra = 0
        rem = 0

        for k in d:
            if z >= d[k]:
                extra += (z-d[k])//2
            else:
                rem += d[k]-z
        if extra >= rem:
            u = inter
        else:
            l = inter + 1

    print(l)
