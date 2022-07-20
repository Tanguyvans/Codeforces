for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    a.reverse()
    b.reverse()

    na = [a[0]]
    nb = [b[0]]

    s = 0
    l = []
    for i in range(1, len(a)):
        aa = 0
        ab = 0
        ba = 0
        bb = 0
        for j in range(len(na)):
            aa += (a[i]+na[j])**2
            ab += (a[i]+nb[j])**2
            ba += (b[i]+na[j])**2
            bb += (b[i]+nb[j])**2

        if aa + bb <= ab + ba:
            s += bb + aa
            na.append(a[i])
            nb.append(b[i])
        else:
            s += ba + ab
            na.append(b[i])
            nb.append(a[i])

    print(l)
    print(s)
