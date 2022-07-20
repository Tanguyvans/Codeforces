for _ in range(int(input())):

    nb = input()

    a = [int(i) for i in nb]

    if len(nb) > 2:
        print(min(a))
    else:
        print(a[-1])
