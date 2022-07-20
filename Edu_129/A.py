for _ in range(int(input())):
    na = int(input())
    a = list(map(int, input().split(' ')))
    nb = int(input())
    b = list(map(int, input().split(' ')))

    if max(a) == max(b):
        print('Alice')
        print('Bob')

    elif max(a) > max(b):
        print('Alice')
        print('Alice')

    else:
        print('Bob')
        print('Bob')
