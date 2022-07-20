import math

for _ in range(int(input())):

    n, r, b = map(int, input().split(' '))

    while r > 0 or b > 0:
        s = math.ceil(r/(b+1))

        print('R'*s, end='')

        if b > 0:
            print('B', end='')

        r -= s
        b -= 1

    print('')
