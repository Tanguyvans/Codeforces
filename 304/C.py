n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s1 = []
ss1 = []
for i in range(a[0]):
    s1.append(a[i+1])
    ss1.append(a[i+1])

s2 = []
ss2 = []
for i in range(b[0]):
    s2.append(b[i+1])
    ss2.append(b[i+1])

impossible = False
nb = 0

old1 = []
old2 = []
while len(s1) > 0 and len(s2) > 0:
    p1 = s1[0]
    del s1[0]
    p2 = s2[0]
    del s2[0]

    if p1 > p2:
        s1.append(p2)
        s1.append(p1)

    else:
        s2.append(p1)
        s2.append(p2)
    nb += 1

    if s1 in old1 and s2 in old2:
        impossible = True
        break

    old1.append(s1[:])
    old2.append(s2[:])

if impossible:
    print(-1)
else:
    if len(s1) > 0:
        print(nb, 1)
    else:
        print(nb, 2)
