for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    odd = 0
    even = 0
    four = 0
    m = a[0]
    for i in range(n):
        m = min(a[i], m)
        if a[i] % 2 != 0:
            odd += 1
        else:
            if int(a[i]/4) != a[i]/4:
                four += 1

            even += 1

    if odd > 0:
        print(n-odd)
    else:
        if four:
            print(n)
        else:
            print(n+2)
