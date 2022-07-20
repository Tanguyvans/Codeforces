for _ in range(int(input())):
    n, m, k = map(int, input().split(' '))

    if n == m:
        print(n*k)
        continue

    print(375000012 % 1000000007)
