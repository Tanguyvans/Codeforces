for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split(' ')))

    tag = [False for i in range(n)]

    g = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i] != a[j]:
                g[i].append(j)

    from collections import deque as dq

    d = dq()
    tag = [False for i in range(n)]

    d.append(0)
    ans = []
    tag[0] = True
    while len(d) > 0:
        pos = d.popleft()
        for i in g[pos]:
            if not tag[i]:
                tag[i] = True
                d.append(i)
                ans.append([pos+1, i+1])

    if len(ans) != n-1:
        print('NO')
    else:
        print("YES")
        for i in range(n-1):
            print(ans[i][0], ans[i][1])
