for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    zeros = set()
    good = set()
    for i in range(1, n):
        if a[i-1] in zeros:
            continue

        if a[i] in zeros:
            ai = 0
        else:
            ai = a[i]

        if a[i-1] > ai:
            zeros.add(a[i-1])
            zeros |= good
            good = set()
        else:
            good.add(a[i-1])

    print(len(zeros))
