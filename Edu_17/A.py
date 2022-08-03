import math
n, k = map(int, input().split())

cnt = 0
d1 = []
d2 = []
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        if i != int(n/i):
            d1.append(i)
            d2.append(int(n/i))
            cnt += 2
        else:
            d1.append(i)
            cnt += 1

d2.reverse()
d = d1 + d2
if k <= cnt:
    print(d[k-1])
else:
    print(-1)
