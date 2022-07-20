n, l, k = map(int, input().split(' '))

d = list(map(int, input().split(' ')))
d.append(l)
a = list(map(int, input().split(' ')))

dd = [0 for i in range(n)]
for i in range(n):
    dd[i] = d[i+1]-d[i]

m = [[0 for j in range(n)] for i in range(k+1)]

for i in range(k+1):
    if i == 0:
        m[i][0] = dd[0]*a[0]
        for j in range(1, n):
            m[i][j] = m[i][j-1]+dd[j]*a[j]

    else:
        for j in range(n):
            if j < i:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-1]+dd[j]*a[j-1])


print(m)
