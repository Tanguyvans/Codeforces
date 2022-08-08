from collections import deque as dq

n = int(input())
if n % 2 != 0:
    print(-1)
else:
    graph = {i: [] for i in range(n)}

    for i in range(n-1):
        x, y = map(int, input().split())

        graph[x-1].append(y-1)
        graph[y-1].append(x-1)

    vis = [-1 for i in range(n)]
    d = dq()

    ans = 0
    for i in range(n):
        if vis[i] == -1 and len(graph[i]) == 1:
            vis[i] = 1
            d.append(i)

            while len(d) > 0:
                pos = d.popleft()
                for k in graph[pos]:
                    if vis[k] == -1 and len(graph[k]) == 2:
                        ans += 1
                        for l in graph[k]:
                            if pos != l:
                                d.append(l)
                                vis[l] = 1
                        vis[k] = 1

    print(ans)
