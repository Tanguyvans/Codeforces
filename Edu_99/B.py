for _ in range(int(input())):
    n = int(input())

    ans = 0
    a = 0
    k = 1
    while True:
        if a < n:
            a += k
            k += 1
            ans += 1
        elif a == n:
            break
        else:
            for i in range(k, 0, -1):
                if a-i > n:
                    ans += 1
                elif a-i == n:
                    if i == 1:
                        ans += 1
                    a = n
                    break
    print(ans)
