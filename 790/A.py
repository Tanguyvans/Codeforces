for _ in range(int(input())):

    a = input()

    sa = 0
    sb = 0

    for i, ai in enumerate(a):

        if i <= 2:
            sa += int(ai)

        else:
            sb += int(ai)

    print("YES" if sa == sb else 'NO')
