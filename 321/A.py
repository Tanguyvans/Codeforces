n = int(input())
a = list(map(int, input().split()))

ans = 0
p = 0
for i in range(1, n):
    if a[i] < a[i-1]:
        ans = max(ans, i-p)
        p = i

ans = max(ans, n-p)

print(ans)
