n = int(input())

a = list(map(int, input().split(' ')))
ans = -1000

for i in range(n):
    for j in range(n-i):
        ans = max(ans, i+1 - sum(a[j:j+i+1])*2)

if sum(a) == n:
    print(n-1)
else:
    print(ans + sum(a))
