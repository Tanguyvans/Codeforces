for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    if a[0] < 0:
        neg = True
        a0 = a[0]
    else:
        neg = False
        a0 = a[0]
    somme = 0
    for i in range(1, n):

        if a[i] < 0 and neg:
            a0 = max(a0, a[i])

        elif a[i] > 0 and neg:
            somme += a0
            neg = False
            a0 = a[i]

        elif a[i] < 0 and not neg:
            somme += a0
            neg = True
            a0 = a[i]

        elif a[i] > 0 and not neg:
            a0 = max(a0, a[i])

    somme += a0

    print(somme)
