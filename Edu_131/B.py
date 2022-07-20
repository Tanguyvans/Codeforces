import math

for _ in range(int(input())):
    n = int(input())

    print(2)

    for i in range(int(math.floor(n/2))):
        print(i+1, (i+1)*2, end=' ')

    if n % 2 != 0:
        print(n)

    print('')
