n, k = map(int, input().split())

if n == 1:
    print(0)
else:
    g = {i: [] for i in range(n)}
    for i in range(n-1):
        x, y, c = map(int, input().split())
        if c == 0:
            g[x-1].append(y-1)
            g[y-1].append(x-1)

    from collections import deque as dq
    d = dq()
    tag = [False for i in range(n)]
    ans = n**k
    for i in range(n):
        if tag[i] == True:
            continue

        d.append(i)
        val = 1
        while len(d) > 0:
            pos = d.popleft()
            tag[pos] = True
            for j in g[pos]:
                if tag[j] == False:
                    tag[j] = True
                    d.append(j)
                    val += 1
        ans -= val**k

    print(ans % (10**9+7))
