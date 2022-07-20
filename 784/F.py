for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    r = n-1
    ans = 0
    l0 = 0
    r0 = 0

    while True:
        if l == r:
            break

        if a[l] + l0 == a[r]+r0:
            ans = l+1 + (n-r)
            l0 += a[l]
            l += 1
        elif a[l] + l0 < a[r]+r0:
            l0 += a[l]
            l += 1
        elif a[l] + l0 > a[r]+r0:
            r0 += a[r]
            r -= 1

    print(ans)
