for _ in range(int(input())):
    w, h, n = map(int, input().split())

    ans = 1
    while w % 2 == 0 or h % 2 == 0:
        if ans >= n:
            break
        if w % 2 == 0:
            w //= 2
            ans *= 2
        if h % 2 == 0:
            h //= 2
            ans *= 2

    if ans < n:
        print('NO')
    else:
        print('YES')
