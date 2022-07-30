for _ in range(int(input())):
    n, a, b = map(int, input().split())

    pos = n % b

    seq = set()

    i = 1
    while True:
        if i % b not in seq and i <= n:
            seq.add(i % b)
            i *= a

        else:
            break

    if pos not in seq:
        print('No')
    else:
        print('Yes')
