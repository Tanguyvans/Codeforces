for _ in range(int(input())):

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    grp = {i: a[i] for i in range(n)}
    print(grp)
    unhappy = sum(a)
    for i in range(m):
        x, y = map(int, input().split())
