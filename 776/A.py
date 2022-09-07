for _ in range(int(input())):
    a = list(input())
    c = input()

    imp = True
    for i in range(len(a)):
        if a[i] == c and i % 2 == 0:
            imp = False
            break

    if imp:
        print('NO')
    else:
        print('YES')
