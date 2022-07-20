for _ in range(int(input())):
    n, c, q = map(int, input().split())

    s = input()

    for i in range(c):
        l, r = map(int, input().split())
        s += s[l-1:r]

    for i in range(q):
        k = int(input())
        print(s[k-1])
