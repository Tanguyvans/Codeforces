def findMin(m, maxl):
    m = n-1
    pm = a[m][1]
    hm = a[m][1]
    wm = a[m][2]
    for i in range(n-1, -1, -1):
        if hm >= a[i][1] and a[i][2] < maxl:
            m = i
            pm = a[i][0]
            hm = a[i][1]
            wm = a[i][2]

    return m, pm, hm, wm


for _ in range(int(input())):
    n = int(input())

    a = []
    for i in range(n):
        h, w = map(int, input().split())

        a.append([i, min(h, w), max(h, w)])

    a = sorted(a, key=lambda x: (x[2], x[1]))
    sol = [-1 for i in range(n)]

    m, pm, hm, wm = findMin(n-1, a[n-1][2])

    for i in range(n-1, -1, -1):
        hi = a[i][1]
        wi = a[i][2]
        if wm < wi:
            if hm < hi:
                sol[a[i][0]] = pm
        else:
            m, pm, hm, wm = findMin(n-i, a[i-1][2])

            if wm < wi and hm < wm:
                sol[a[i][0]] = pm

    for si in sol:
        if si == -1:
            print(-1, end=' ')
        else:
            print(si+1, end=' ')

    print()
