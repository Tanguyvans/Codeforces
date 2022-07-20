for _ in range(int(input())):
    n, m = map(int, input().split())

    a = []
    x = 0
    y = 0
    maxi = -10**10
    for i in range(n):
        ai = list(map(int, input().split()))
        for j in range(m):
            if ai[j] >= maxi:
                y = i
                x = j
                maxi = ai[j]

    print(min(max(x+1, m-x), m)*min(max(y+1, n-y), n))
