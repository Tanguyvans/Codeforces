for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = dict()
    mina = a[0]
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
        mina = min(a[i], mina)

    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    seq = [-1 for i in range(n+1)]

    if mina == 0:
        seq[0] = d[mina]
    elif mina > 1:
        seq[0] = 0

    for i in range(1, n):
        if a[i] > i:
            seq[i] = seq[i-1] - 1

            break

        if si == s:
            seq[i] = 1
        else:
            seq[i] = si-s-1

    print(seq)
