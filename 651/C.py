import math

for _ in range(int(input())):
    n = int(input())

    pos = False
    for i in range(2, math.ceil(n**(1/2))):
        if n/i == int(n/i):
            if i % 2 != 0:
                pos = True
            elif n/i % 2 != 0 and i > 2:
                pos = True

    if n != 1 and n % 2 != 0:
        print('Ashishgup')
    elif n % 2 == 0 and pos:
        print('Ashishgup')
    elif n == 2:
        print('Ashishgup')
    else:
        print('FastestFinger')
