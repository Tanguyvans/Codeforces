
n, l, k = map(int, input().split(' '))
d = list(map(int, input().split(' ')))
d.append(l)
a = list(map(int, input().split(' ')))

v = [a[i]*(d[i+1]-d[i]) for i in range(len(a))]
#s = [d[i+1]-d[i] for i in range(len(d)-1) ]
for i in range(k):
    delta = 0
    pos = 0
    for j in range(1, len(v)):
        if v[j]-(d[j+1]-d[j])*a[j-1] >= delta:
            delta = v[j]-(d[j+1]-d[j])*a[j-1]
            pos = j
            dist = d[j+1]-d[j]

    if delta <= 0:
        break

    v[pos-1] = v[pos] + v[pos-1] - delta
    d[pos] += dist
    del v[pos]
    del d[pos+1]

print(sum(v))
