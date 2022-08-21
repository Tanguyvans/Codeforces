for _ in range(int(input())):
    n, m = map(int, input().split())

    k = list(map(int, input().split()))
    k = sorted(k, reverse=True)
    c = list(map(int, input().split()))

    disp = 0
    ans = 0
    for i in range(n):
        if disp < k[i]-1:
            ans += c[disp]
            disp += 1
        else:
            ans += c[k[i]-1]

    print(ans)
