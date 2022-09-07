n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

if k > 0:
    m = a[k-1]
    if k == n:
        print(m)
    else:
        if a[k] == m:
            print(-1)
        else:
            print(m)

else:
    print(-1 if a[0] == 1 else a[0]-1)
