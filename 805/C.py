sol = []
for _ in range(int(input())):
    input()

    n, k = map(int, input().split())
    u = list(map(str, input().split()))

    d = {}
    for i in range(n):
        if u[i] not in d:
            d[u[i]] = [i, i]
        else:
            d[u[i]][1] = i

    for i in range(k):
        a, b = map(str, input().split())

        if a in d and b in d and d[a][0] < d[b][1]:
            print('YES')
        else:
            print('NO')
