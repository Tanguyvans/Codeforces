n, m = map(int, input().split())
a = list(map(int, input().split()))

sol = [0 for i in range(n)]
distinct = set()
sol[-1] = 1
distinct.add(a[-1])
for i in range(n-2, -1, -1):
    if a[i] not in distinct:
        sol[i] = sol[i+1] + 1
        distinct.add(a[i])
    else:
        sol[i] = sol[i+1]

for i in range(m):
    pos = int(input())
    print(sol[pos-1])
