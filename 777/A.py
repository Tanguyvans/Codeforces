for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        if n % 2 == 0:
            flag = True
        else:
            flag = False

        while n != 0:
            if flag:
                print(1, end='')
                n -= 1
                flag = False
            else:
                print(2, end='')
                n -= 2
                flag = True

        print()
