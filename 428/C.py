from collections import deque as dq
n = int(input())

if n == 1:
    print(0)
else:
    g = {i: [] for i in range(n)}

    for i in range(n-1):
        x, y = map(int, input().split())

        g[x-1].append(y-1)
        g[y-1].append(x-1)

    d = dq()

    # [prob, pos, l]
    d.append([1, 0, 0])
    tag = [False for i in range(n)]
    ans = 0
    while len(d) > 0:
        prob, pos, l = d.popleft()
        tag[pos] = True
        if pos == 0:
            prob = prob*1/len(g[pos])
        else:
            prob = prob*1/max(1, len(g[pos])-1)

        next = False
        for i in g[pos]:
            if tag[i] == False:
                d.append([prob, i, l+1])
                tag[i] = True
                next = True
        if not next:
            #ans.append([prob, l])
            ans += prob*l

    print(ans)
