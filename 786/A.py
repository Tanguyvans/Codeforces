for _ in range(int(input())):
    x, y = map(int, input().split(' '))

    b = y/x

    if b != int(b):
        print(0, 0)
    else:
        print(1, int(b))
