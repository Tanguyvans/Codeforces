

for _ in range(int(input())):
    a = int(input())
    a = bin(a)

    sol = ''
    an = False
    xo = False
    print(a)
    for i in a[::-1]:
        if i == '1' and an == False:
            sol = '1' + sol
            an = True

        elif i == '1':
            sol = '0' + sol
            xo = True

        else:
            if xo == False:
                sol = '1' + sol
                xo = True
            else:
                sol = '0' + sol

        if an == True and xo == True:
            break

    if xo == False:
        sol = '1' + sol

    print(int(sol, 2))
