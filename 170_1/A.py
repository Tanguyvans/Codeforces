from collections import deque as dq


def dfs(g, n, m):
    tag = [False for i in range(n+m)]
    j = 0
    for i in range(n):
        if tag[i] == False:
            j += 1
            dfsHelper(i, g, tag, j)

    return tag


def dfsHelper(pos, g, tag, val):
    tag[pos] = val
    for i in g[pos]:
        if tag[i] == False:
            dfsHelper(i, g, tag, val)


n, m = map(int, input().split())
g = [[] for i in range(n+m)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, len(a)):
        g[i].append(n+a[j]-1)
        g[n+a[j]-1].append(i)

tag = dfs(g, n, m)
if not any(tag[n:]):
    print(max(tag[:n]))
else:
    print(max(tag[:n])-1)
