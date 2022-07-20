for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    ans = 0

    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        for i in range(a[0]+a[1], a[-2]+a[-1]):
            b = a[:]
            sol = 0
            j = 0
            while True:
                for k in range(j, len(b)):
                    if j != k:
                        if b[j] + b[k] == i:
                            sol += 1
                            del b[k]
                            break
                if j >= len(b)-1:
                    break
                j += 1
            ans = max(ans, sol)

        print(ans)
