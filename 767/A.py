for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))

    ab = []
    for ai, bi in zip(a, b):
        ab.append([ai, bi])

    ab = sorted(ab, key=lambda x: (x[0], x[1]))

    for i in ab:
        if i[0] <= k:
            k += i[1]

    print(k)
