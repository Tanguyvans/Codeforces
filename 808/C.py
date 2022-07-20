for _ in range(int(input())):
    n, q = map(int, input().split())

    a = list(map(int, input().split()))

    sol = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        if a[i] <= q:
            if i == n-1:
                sol[i] = 1
            else:
                sol[i] = max(min(a[i], n-i), sol[i+1])

    min_q = 0
    for i in range(n-1, -1, -1):
        min_q = max(min_q, sol[i])
        if sol[i] == 0:
            if i == n-1 and q > 0:
                sol[i] = 1
                min_q = 1
            elif q-min_q >= sol[i+1]:
                sol[i] = sol[i+1] + 1
                min_q += 1

    for i in range(n):
        if sol[i] == 0:
            print(0, end='')
        else:
            print(1, end='')

    print()
