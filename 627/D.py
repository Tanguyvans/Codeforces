from collections import Counter

n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

c = [a[i]-b[i] for i in range(n)]

c = sorted(c)

l = 0
u = n-1
ans = 0
while l < n-1:
    if c[l] + c[u] > 0:
        if c[l] + c[u-1] > 0 and l < u:
            u -= 1
            continue
        else:
            if u <= l:
                u = l+1
            ans += n-u
            l += 1

    else:
        l += 1

print(ans)
