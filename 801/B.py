for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    winner = ''
    for i in range(1, n):
        if a[i-1] > a[i] > 1:
            if i % 2 == 0:
                winner = 'even'
            else:
                winner = 'odd'
        else:
            a[i] -= a[i-1]

    if winner == 'even':
        print('Mike')
    elif winner == 'odd':
        print('Joe')

    else:
        if n % 2 == 0:
            print('Joe')
        else:
            print('Mike')
