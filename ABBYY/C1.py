from collections import deque as dq

n = int(input())
k = int(input())

friends = {i: [] for i in range(n)}

for i in range(k):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

m = int(input())
enemies = {i: [] for i in range(n)}

for i in range(m):
    a, b = map(int, input().split())
    enemies[a-1].append(b-1)
    enemies[b-1].append(a-1)

d = dq()

pf = {i: -1 for i in range(n)}
vf = [-1 for i in range(n)]
nb = 0
for i in range(n):
    if vf[i] == -1:
        vf[i] = nb
        d.append(i)
        pf[i] = nb
        while len(d) > 0:
            pos = d.popleft()
            for j in friends[pos]:
                if vf[j] == -1:
                    pf[j] = nb
                    vf[j] = nb
                    d.append(j)

        nb += 1

nb = 0
sol = 0
ans = 0
for i in range(n):
    if vf[i] == nb:
        for j in enemies[i]:
            if vf[j] == vf[i]:
                sol = -1

        if sol == -1:
            nb += 1
            sol = 0
        else:
            sol += 1
    else:
        ans = max(ans, sol)

ans = max(ans, sol)
print(ans)
