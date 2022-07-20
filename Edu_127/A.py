from math import fabs


for _ in range(int(input())):

    w = input()

    a = 0
    b = 0
    curent = w[0]

    if curent == 'a':
        a += 1
    elif curent == "b":
        b += 1

    flag = False
    for i in w[1:]:
        if i == 'a' and curent == i:
            a += 1
        elif i == 'b' and curent == i:
            b += 1
        elif i == 'a' and curent != i:
            if b == 1:
                flag = True
                break
            else:
                b = 0
                curent = 'a'
                a += 1

        elif i == 'b' and curent != i:
            if a == 1:
                flag = True
                break
            else:
                a = 0
                curent = 'b'
                b += 1

    if flag or a == 1 or b == 1:
        print('NO')
    else:
        print('YES')
