for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    seg = []
    for i in range(1, m):
        seg.append(a[i]-a[i-1]-1)

    seg.append(a[0]+n-a[m-1]-1)

    seg = sorted(seg, reverse=True)

    saved = 0
    spread = 0
    for i in range(m):
        if seg[i]-1 > spread*2:
            saved += seg[i] - spread*2 - 1
            spread += 2
        elif seg[i]-1 == spread*2:
            saved += 1
            break

        else:
            break

    print(n-saved)
