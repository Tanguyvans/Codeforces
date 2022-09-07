for _ in range(int(input())):
    a = input()
    a = [i for i in a]
    n = len(a)
    ans = 0
    d = set()

    for i in range(n):
        ai = a[i]

        if d:
            if ai in d:
                ans += 2
                d = set()
            else:
                d.add(ai)

        else:
            d.add(ai)

    print(n-ans)
