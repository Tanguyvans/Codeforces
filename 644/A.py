for _ in range(int(input())):
    a, b = map(int, input().split())

    if 2*a >= b and 2*b >= a:
        print(min((2*a)**2, (2*b)**2))
    else:
        print(max((a)**2, (b)**2))
