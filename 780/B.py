for _ in range(int(input())):
    n = int(input())
    candles = list(map(int, input().split(' ')))

    candles = sorted(candles, reverse=True)

    if len(candles) == 1:
        if candles[0] > 1:
            print('NO')
        else:
            print('YES')

    else:
        if candles[0] > candles[1] + 1:
            print('NO')
        else:
            print('YES')
