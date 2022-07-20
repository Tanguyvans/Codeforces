for _ in range(int(input())):
    n = int(input())

    ans = 0

    while 10**ans <= n:
        ans += 1

    print(n-10**(ans-1))
