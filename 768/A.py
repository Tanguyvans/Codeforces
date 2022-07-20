for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    for i, (ai, bi) in enumerate(zip(a, b)):

        if ai < bi:
            inter = a[i]
            a[i] = b[i]
            b[i] = inter

    print(max(a)*max(b))
