for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split(' ')))
    smallEven = -1
    smallOdd = -1
    Imp = False
    for nb in numbers:
        if nb % 2 == 0:
            if smallEven <= nb:
                smallEven = nb
            else:
                Imp = True
        else:
            if smallOdd <= nb:
                smallOdd = nb
            else:
                Imp = True
        if Imp == True:
            break

    if Imp:
        print('No')
    else:
        print('Yes')
