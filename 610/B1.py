for _ in range(int(input())):
    n, p, k = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    a = sorted(a)

    if a[0] > p:
        print(0)
    else:
        ans = 1
        if a[1] > p:
            print(ans)
        else:
            ans += 1
            f2 = a[0]
            f1 = a[1]
            for i in range(2, n):
                if i % 2 == 0:
                    if f2 + a[i] <= p:
                        ans += 1
                        f2 += a[i]
                    else:
                        break
                else:
                    if f1 + a[i] <= p:
                        ans += 1
                        f1 += a[i]
                    else:
                        break

            print(ans)
