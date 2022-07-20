for _ in range(int(input())):
    n = int(input())

    s = input()

    c1 = 0
    c0 = 0
    ans = 0
    nb = 1
    si_1 = s[0]

    impair = False
    add = False

    if si_1 == '0':
        c0 += 1
    else:
        c1 += 1

    for si in s[1:]:
        if si_1 == '1' and si == '1':
            c1 += 1
        elif si_1 == '0' and si == '0':
            c0 += 1
        elif si_1 == '1' and si == '0':
            if impair:
                if c1 % 2 != 0:
                    ans += 1

                    if c1 > 1:
                        nb += 1
                else:
                    ans += 2
                    c0 += 1

                    if c1 > 2:
                        nb += 1

                impair = False
            else:

                if c1 % 2 != 0:
                    impair = True
                else:
                    nb += 1

            c0 += 1
            c1 = 0
        elif si_1 == '0' and si == '1':
            if impair:
                if c0 % 2 != 0:
                    ans += 1

                    if c0 > 1:
                        nb += 1
                else:
                    ans += 2
                    c1 += 1

                    if c0 > 2:
                        nb += 1
                impair = False
            else:
                if c0 % 2 != 0:
                    impair = True
                else:
                    nb += 1

            c0 = 0
            c1 += 1

        si_1 = si

    if c1 % 2 != 0 or c0 % 2 != 0:
        if c1 == 1 or c0 == 1:
            print(ans+1, nb+1)
        else:
            print(ans+1, nb+1)
    else:
        print(ans, nb)
