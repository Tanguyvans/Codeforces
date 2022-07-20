for _ in range(int(input())):
    n = int(input())

    if n % 2 != 0:
        print('YES')
    else:
        while n % 2 == 0 and n > 2:
            n //= 2

        if n == 2:
            print('NO')
        else:
            print('YES')
