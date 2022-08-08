n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = float('inf')
for j in range(1, n-1):
    sj = s[j]
    cj = c[j]

    ci = float('inf')
    ck = float('inf')

    for i in range(j):
        if s[i] < sj:
            ci = min(ci, c[i])

    for k in range(j+1, n):
        if s[k] > sj:
            ck = min(ck, c[k])

    ans = min(ans, ci+cj+ck)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
