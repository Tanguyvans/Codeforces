d, sch = map(int, input().split())

fl = 0
cl = 0

f = []
c = []

for i in range(d):
    a, b = map(int, input().split())
    f.append(a)
    c.append(b)

    fl += a
    cl += b

if sch < fl or sch > cl:
    print('NO')

else:
    s = 0
    print('YES')
    dl = sch - fl
    for i in range(d):
        if c[i] < f[i]+dl:
            dl -= c[i]-f[i]
            print(c[i], end=' ')
            s += c[i]
        else:
            print(f[i]+dl, end=' ')
            s += f[i]+dl
            dl = 0

    print('')
