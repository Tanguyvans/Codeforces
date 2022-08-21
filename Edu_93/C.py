for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))

    r = 0
    ans = 0
    d = {0: 1}

    for i in range(n):
        r += a[i]

        s = r - i - 1
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

        ans += d[s] - 1

    print(ans)
