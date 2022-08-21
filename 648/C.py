n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

seq = {}

for i in range(n):
    seq[a[i]] = i

sol = {}
ans = 0
for i in range(n):
    if seq[b[i]]-i > 0:
        div = seq[b[i]]-i
    else:
        div = n-i+seq[b[i]]

    if div not in sol:
        sol[div] = 1
    else:
        sol[div] += 1

    ans = max(sol[div], ans)

print(ans)
