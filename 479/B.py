n = int(input())
a = list(input())
d = {}

ans = 0
sol = ''
for i in range(n-1):
    ai = a[i] + a[i+1]

    if ai in d:
        d[ai] += 1
    else:
        d[ai] = 1

    if d[ai] > ans:
        ans = d[ai]
        sol = ai

print(sol)
