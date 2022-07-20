from collections import deque as dq

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    g = [[] for i in range(n)]
    for i in range(n):
        g[a[i]-1].append(i)

    d = dq()
    tag = [False for i in range(n)]
    cycle = {}
    ans = [[] for i in range(n)]
    for i in range(n):
        if not tag[i]:
            d.append(i)
            tag[i] = True
            cycle[i] = 1
            ans[i] = i

        while len(d) > 0:
            pos = d.popleft()
            for j in g[pos]:
                if not tag[j]:
                    tag[j] = True
                    cycle[i] += 1
                    ans[j] = i
                    d.append(j)

    for i in range(n):
        print(cycle[ans[i]], end=' ')

    print('')
