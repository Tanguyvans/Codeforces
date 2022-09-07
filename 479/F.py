n = int(input())
a = list(map(int, input().split()))

d = {}
ans = 0
m = 0
for i in range(n):
    if a[i]-1 in d:
        d[a[i]] = d[a[i]-1]+1
    else:
        d[a[i]] = 1

    if d[a[i]] > ans:
        ans = d[a[i]]
        m = a[i]

print(ans)
mn = m-ans+1
for i in range(n):
    if a[i] == mn:
        print(i+1, end=' ')
        mn += 1
        if mn > m:
            break
