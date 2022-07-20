n, k = map(int, input().split())

s = input()

c = list(map(str, input().split()))

ans = 0
nb = 0
for i in range(n):
    if s[i] in c:
        nb += 1
    else:
        ans += nb*(nb+1)//2
        nb = 0

ans += nb*(nb+1)//2

print(ans)
