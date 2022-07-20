for _ in range(int(input())):
    n, x, y = map(int, input().split())
    alice = x
    bob = x + 3

    numbers = list(map(int, input().split(' ')))

    countOdd = 0
    for num in numbers:
        if num % 2 != 0:
            countOdd += 1

    if (y-alice) % 2 == 0:
        if countOdd % 2 == 0:
            print('Alice')
        else:
            print('Bob')
    else:
        if countOdd % 2 == 0:
            print('Bob')
        else:
            print('Alice')
