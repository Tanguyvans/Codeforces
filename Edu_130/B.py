n, q = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
b = [0]
for i in range(n):
    b.append(b[-1]+a[i])

for i in range(q):
    x, y = map(int, input().split())
    print(b[x]-b[x-y])
