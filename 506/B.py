n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
m = 1
for i in range(1, n):
    if a[i-1]*2 >= a[i]:
        m += 1
    else:
        ans = max(ans, m)
        m = 1

ans = max(ans, m)
print(ans)
