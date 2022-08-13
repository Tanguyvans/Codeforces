from collections import deque as dq

n = int(input())

graph = {i: [] for i in range(n)}

a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n-1):
    graph[a[i]-1].append(i+1)

d = dq()
d.append([b[0], 0])
ans = 1
while len(d) > 0:
    color, pos = d.popleft()
    for k in graph[pos]:
        if b[k] != color:
            ans += 1

        d.append([b[k], k])

print(ans)
