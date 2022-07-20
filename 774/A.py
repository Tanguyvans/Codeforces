for _ in range(int(input())):
    n, s = map(int, input().split(' '))
    n_2 = n**2

    if s == 0:
        print(0)
    elif n >= s and n != 1:
        print(0)
    else:
        print(s//n_2)
