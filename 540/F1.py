n = int(input())
a = list(map(int, input().split()))

g = {i: [] for i in range(n)}

for i in range(n-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

print(g)
