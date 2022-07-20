import math
for _ in range(int(input())):
    n, m = map(int, input().split(' '))

    grid = [['W' for i in range(m)] for j in range(n)]
    for k in range(n*(m-1)):
        if k == 0:
            print(abs(int(math.ceil(n/2))-n) +
                  abs(int(math.ceil(m/2)-m)), end='')
            continue

        grid

    print('')
