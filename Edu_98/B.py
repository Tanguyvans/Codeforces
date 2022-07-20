for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    a = sorted(a, reverse=True)
    s = sum(a)
    m = a[0]
    tot = m*(n-1)

    print(abs(tot-s))
