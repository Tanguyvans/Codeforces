for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sol = ['B' for i in range(m)]

    for i in range(n):
        p1 = min(a[i], m-a[i]+1)
        p2 = max(a[i], m-a[i]+1)
        if sol[p1-1] == 'B':
            sol[p1-1] = 'A'
        elif sol[p2-1] == 'B':
            sol[p2-1] = 'A'

    print(''.join(sol))
