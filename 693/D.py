for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a = sorted(a, reverse=True)

    alice = 0
    bob = 0

    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 0:
                alice += a[i]
        else:
            if a[i] % 2 != 0:
                bob += a[i]

    if alice == bob:
        print('Tie')
    elif alice > bob:
        print('Alice')
    else:
        print('Bob')
