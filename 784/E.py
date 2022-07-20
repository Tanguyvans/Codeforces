for _ in range(int(input())):
    n = int(input())

    d = {}

    for i in range(n):
        a = input()
        if a[0]+'.' in d:
            d[a[0]+'.'] += 1
        else:
            d[a[0]+'.'] = 1

        if '.'+a[1] in d:
            d['.'+a[1]] += 1
        else:
            d['.'+a[1]] = 1

        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    ans = 0
    for k, v in d.items():
        if '.' in k:
            continue

        ans += v * (d[k[0]+'.']-v)
        d[k[0]+'.'] -= v
        ans += v * (d['.'+k[1]]-v)
        d['.'+k[1]] -= v

    print(ans)
