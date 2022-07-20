for _ in range(int(input())):
    l1, r1, l2, r2, = map(int, input().split(' '))

    if l1 <= r2 and l2 <= r1:
        print(max(l1, l2))

    else:
        print(l1+l2)
