from audioop import reverse


for _ in range(int(input())):

    n, k = map(int, input().split(' '))
    s = input()
    revs = s[::-1]

    if s == revs or k == 0:
        print('1')
    else:
        print('2')
