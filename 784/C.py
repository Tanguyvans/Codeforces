for _ in range(int(input())):

    n = int(input())
    nb = list(map(int, input().split(' ')))

    oO = 0
    oE = 0

    eO = 0
    eE = 0

    for i in range(len(nb)):

        if (i+1) % 2 == 0 and nb[i] % 2 == 0:
            eE = 1
        elif (i+1) % 2 == 0 and nb[i] % 2 != 0:
            eO = 1
        elif (i+1) % 2 != 0 and nb[i] % 2 == 0:
            oE = 1
        else:
            oO = 1

        if oO == oE == 1 or eO == eE == 1:
            break

    if oE != oO and eO != eE:
        print('YES')
    else:
        print('NO')
