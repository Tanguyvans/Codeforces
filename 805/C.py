for _ in range(int(input())):
    input()

    n, k = map(int, input().split())
    u = list(map(int, input().split()))

    d = {}
    for i in range(n):
        if u[i] not in d:
            d[u[i]] = [i]
        elif len(d[u[i]]) < 2:
            d[u[i]].append(i)
        else:
            d[u[i]] = [d[u[i]][0], i]
    for i in range(k):
        a, b = map(int, input().split())
        if a in d and b in d:
            if min(d[a]) < max(d[b]):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
