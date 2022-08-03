for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ones = False
    twos = False
    for i in range(n):
        if str(a[i])[-1] != '0' and str(a[i])[-1] != '5':
            if ones:
                twos = True
                break
            else:
                while str(a[i])[-1] != '2':
                    a[i] += int(str(a[i])[-1])

                a[i] = a[i] % 20
        else:
            if twos:
                ones = True
                break

    imp = False
    if ones and twos:
        imp = True
    elif twos:
        a0 = a[0]
        for i in range(1, n):
            if a[i] != a0:
                imp = True
                break
    else:
        ten = -1
        five = -1
        for i in range(n):
            if a[i] % 10 != 0:
                if five == ten == -1 or (five == -1 and a[i]+5 == ten):
                    five = a[i]
                elif five != a[i]:
                    imp = True
                    break

            else:
                if five == ten == -1 or (ten == -1 and a[i] == five+5):
                    ten = a[i]
                elif ten != a[i]:
                    imp = True
                    break

    if imp:
        print('No')
    else:
        print('Yes')
