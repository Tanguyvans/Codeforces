for _ in range(int(input())):

    n, a, b = map(int, input().split(' '))

    c = list(map(int, input().split(' ')))

    sc = sum(c)

    ans = b*sc

    for i in range(n):
        sc -= c[i]
        val = (a+b)*c[i] + b*(sc-c[i]*(len(c)-i-1))
        if val <= ans:
            ans = val

    print(ans)
