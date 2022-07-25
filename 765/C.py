n, l, k = map(int, input().split(' '))
d = list(map(int, input().split(' ')))
d.append(l)
d = [d[i]-d[i-1] for i in range(1, n+1)]
a = list(map(int, input().split(' ')))

sol = [[0 for i in range(n+1)] for j in range(k+1)]

for i in range(k+1):
    for j in range(i+1, n+1):
        sol[i][j] = sol[i][j-1]+a[j-1]*d[j-1]

        for m in range(i, j):
            print(m)


print(sol)
