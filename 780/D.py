for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    ai = 1
    j = n-1
    aj = 1

    while i != j:
        fwd = False
        if a[i] >= 1:
            ai *= a[i]
            i += 1

        if a[j] >= 1:
            aj *= a[j]
            j -= 1
