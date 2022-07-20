for _ in range(int(input())):
    x = int(input())
    s = list(map(int, input()))

    sl = 0
    l = 0
    ans = len(s)
    for i in range(x):
        sl = i+1
        r = len(s)
        for j in range(int(s[i])-1):
            if len(s) < x:
                s += s[sl:r]
            else:
                break

        ans = (ans + (int(s[i])-1)*(ans-sl)) % 1000000007

    print(ans)
