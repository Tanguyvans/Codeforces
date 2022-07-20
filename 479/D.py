from collections import deque as dq
n = int(input())
a = list(map(int, input().split()))

g = {a[i]: [] for i in range(n)}

s = {a[i]: [] for i in range(n)}

for i in range(n):
    for j in range(n):
        if a[i] * 2 == a[j]:
            g[a[i]].append(a[j])
        if a[i] == a[j]*3:
            g[a[i]].append(a[j])

        if a[i] == a[j]*2:
            s[a[i]].append(a[j])
        if a[i] * 3 == a[j]:
            s[a[i]].append(a[j])

start = 0
for k, v in s.items():
    if not v:
        start = k
        break

sol = [start]

while True:
    if g[sol[-1]]:
        sol.append(g[sol[-1]][0])

    else:
        break

for i in range(n):
    print(sol[i], end=' ')
