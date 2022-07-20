for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        nb, seq = map(str, input().split())

        sol = a[i]

        for seqi in seq:
            if seqi == 'D':
                sol = (sol+1) % 10
            else:
                sol = sol - 1 if sol - 1 >= 0 else 9

        print(sol, end=' ')

    print()
