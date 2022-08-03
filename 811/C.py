for _ in range(int(input())):
    t = int(input())

    ans = ""
    m = 9
    while t > 0:
        if t >= m:
            ans = str(m) + ans
            t -= m
            m -= 1

        else:
            ans = str(t) + ans
            t = 0

    print(ans)
