for _ in range(int(input())):
    a, b, c, x, y = map(int, input().split())

    s1 = max(0, x - a)
    s2 = max(0, y - b)

    if c >= s1 + s2:
        print('YES')
    else:
        print('NO')
