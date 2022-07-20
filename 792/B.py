for i in range(int(input())):
    a, b, c = map(int, input().split(' '))

    z = c

    y = b + z * 10**8

    x = a + y

    print(x, y, z)
