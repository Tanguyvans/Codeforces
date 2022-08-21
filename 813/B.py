for _ in range(int(input())):
    n = int(input())

    s = 1
    if n % 2 != 0:
        print(1, end=' ')
        s = 2

    for i in range(s, n+1, 2):
        print(i+1, i, end=" ")

    print('')
