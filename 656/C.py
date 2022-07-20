for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a0 = a[-1]
    ans = 0
    up = False
    v = 0
    down = False
    s = False
    for i in range(n-1, -1, -1):
        if a0 < a[i]:
            if not up:
                up = True
                down = False
                v += 1
        if a0 > a[i]:
            if not down:
                down = True
                up = False
                v += 1

        if up and v >= 2:
            ans = i+1
            break

        if down and v >= 3:
            ans = i+1
            break

        a0 = a[i]

    print(ans)
