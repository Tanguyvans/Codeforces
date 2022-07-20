from collections import deque as dq

n = int(input())

pos = []
for i in range(n):
    x, y = map(int, input().split())
    pos.append((x-1, y-1))

d = dq()
vis = [-1 for i in range(n)]
ans = -1
for i in range(n):
    if vis[i] == -1:
        ans += 1
        vis[i] = ans
        d.append(pos[i])

        while len(d) > 0:
            x, y = d.popleft()
            for j, [a, b] in enumerate(pos):
                if (a == x or b == y) and vis[j] == -1:
                    d.append([a, b])
                    vis[j] = ans

print(ans)
