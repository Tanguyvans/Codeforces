for _ in range(int(input())):
    a1, a2 = map(int, input().split())
    a3, a4 = map(int, input().split())

    a = a1+a2+a3+a4
    c1 = a1+a3
    c2 = a2+a4

    r1 = a1+a2
    r2 = a3+a4

    if a == 0:
        print(0)
    elif a <= 3:
        print(1)
    else:
        print(2)
